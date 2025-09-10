import streamlit as st
from pathlib import Path
import json
import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import re
import datetime

# ========== Load models ==========
@st.cache_resource
def load_models():
    emo_model = "bhadresh-savani/distilbert-base-uncased-emotion"
    tokenizer_em = AutoTokenizer.from_pretrained(emo_model)
    model_em = AutoModelForSequenceClassification.from_pretrained(emo_model)
    emo_pipe = pipeline("text-classification", model=model_em, tokenizer=tokenizer_em, return_all_scores=True)

    embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return emo_pipe, embedder

emo_pipe, embedder = load_models()

# ========== Load corpus ==========
corpus_path = Path("corpus.json")
with open(corpus_path, "r", encoding="utf-8") as f:
    corpus = json.load(f)

templates = [c["template"] for c in corpus]
emotions = [c["emotion"] for c in corpus]

embs = embedder.encode(templates, convert_to_numpy=True)
faiss.normalize_L2(embs)
index = faiss.IndexFlatIP(embs.shape[1])
index.add(embs)

# ========== Helper functions ==========
DISCLAIMER = "⚠️ I’m not a therapist; please seek professional help for serious issues. If you're in immediate danger, contact local emergency services."

def clean_text(s):
    s = re.sub(r"http\S+", "", str(s))
    s = re.sub(r"\s+", " ", s).strip()
    return s

def retrieve_templates(user_text, detected_emotion, top_k=3):
    q = embedder.encode([user_text], convert_to_numpy=True)
    faiss.normalize_L2(q)
    D, I = index.search(q, top_k * 3)
    res = []
    for idx in I[0]:
        if idx < 0 or idx >= len(templates):
            continue
        if emotions[idx].lower() == detected_emotion.lower():
            res.append(templates[idx])
        if len(res) >= top_k:
            break
    if not res:
        res = [templates[i] for i in I[0][:top_k]]
    return res

def empathy_pipeline(user_text, memory=None):
    txt = clean_text(user_text)
    scores = emo_pipe(txt)[0]
    top = max(scores, key=lambda x: x['score'])
    emotion = top['label']
    templates_found = retrieve_templates(txt, emotion, top_k=1)

    # إذا الميموري شغال، نضيف التاريخ القديم في الرد
    memory_context = ""
    if memory:
        memory_context = "\n\n(Previous context: " + " | ".join([m for m in memory if m]) + ")"

    response = templates_found[0] + memory_context + "\n\n" + DISCLAIMER
    return emotion, response


# ========== Streamlit UI ==========
st.set_page_config(page_title="EmpathyBot — Sentiment Driven Chat", page_icon="🤖")

st.title("🤖 EmpathyBot — Sentiment Driven Chat (Prototype)")
st.caption(DISCLAIMER)

# Session state init
if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []
if "use_memory" not in st.session_state:
    st.session_state.use_memory = False

# Sidebar controls
st.sidebar.header("⚙️ Chat Settings")
if st.sidebar.button("🔄 Restart Chat"):
    # حفظ المحادثة في الهيستوري
    if st.session_state.messages:
        st.session_state.history.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": st.session_state.messages.copy()
        })
    st.session_state.messages = []

st.session_state.use_memory = st.sidebar.checkbox("Enable Memory", value=st.session_state.use_memory)

# Show history
st.sidebar.subheader("📜 Chat History")
if st.session_state.history:
    for i, chat in enumerate(st.session_state.history[::-1]):
        with st.sidebar.expander(f"Chat {len(st.session_state.history)-i} ({chat['timestamp']})"):
            for role, msg in chat["messages"]:
                st.write(f"**{role.capitalize()}**: {msg}")

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # memory context لو شغال
    memory_context = [m for r, m in st.session_state.messages if r == "user"] if st.session_state.use_memory else []
    emotion, response = empathy_pipeline(user_input, memory=memory_context)

    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("bot", response))

# Show chat
for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
