# 🤖 EmpathyBot: Sentiment-Driven Chat with Advanced RAG

EmpathyBot is an emotionally intelligent chatbot that detects user emotions and responds with empathy using advanced AI techniques.  
It combines **emotion detection**, **retrieval-augmented generation (RAG)**, and a **safety layer** to provide compassionate and context-aware interactions.

---

## 🌟 Features

- **Emotion Detection**: Identifies 6+ emotions (joy, sadness, anger, fear, surprise, love).
- **Empathetic Responses**: Generates contextually relevant, compassionate replies.
- **Advanced RAG**: FAISS-powered retrieval for high-quality response templates.
- **Two Interfaces**: Web UI (Streamlit) and REST API (FastAPI).
- **Real-time Analysis**: Tracks detected emotions with confidence scores.
- **Safety Layer**: Built-in disclaimers for ethical use.

---

## 🚀 Quick Start

### Option 1: Google Colab (Recommended)
1. Open a new Colab notebook  
2. Copy and paste the project code  
3. Run all cells  
4. Choose deployment (Streamlit or FastAPI)

### Option 2: Local Installation
```bash
# Clone the repository
git clone https://github.com/your-username/empathybot.git
cd empathybot

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
