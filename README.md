🤖 EmpathyBot: Sentiment-Driven Chat with Advanced RAG
EmpathyBot is an emotionally intelligent chatbot that detects user emotions and responds with empathy using advanced AI techniques.It combines emotion detection, retrieval-augmented generation (RAG), and a safety layer to provide compassionate and context-aware interactions.
🌟 Features

Emotion Detection: Identifies 6+ emotions (joy, sadness, anger, fear, surprise, love).
Empathetic Responses: Generates contextually relevant, compassionate replies.
Advanced RAG: FAISS-powered retrieval for high-quality response templates.
Two Interfaces: Web UI (Streamlit) and REST API (FastAPI).
Real-time Analysis: Tracks detected emotions with confidence scores.
Safety Layer: Built-in disclaimers for ethical use.

🚀 Quick Start
Option 1: Google Colab (Recommended)

Open a new Colab notebook  
Copy and paste the project code  
Run all cells  
Choose deployment (Streamlit or FastAPI)

Option 2: Local Installation
# Clone the repository
git clone https://github.com/your-username/empathybot.git
cd empathybot

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

📊 Testing Results

Emotion Detection Accuracy: 80%+ on evaluation dataset
Response Appropriateness: 80%+ in manual review
Response Speed: ~2 seconds per query
Corpus Size: 1,000+ empathetic templates across 7 emotion categories

🔧 Architecture
Core Components

Emotion Detection — DistilBERT fine-tuned on tweet_eval:emotion dataset.
RAG System — FAISS-based similarity search over empathetic responses.
Few-Shot Prompting — Combines retrieved templates into final responses.
Safety Layer — Ethical disclaimers and self-harm keyword detection.

Technology Stack

Hugging Face Transformers
Sentence Transformers
FAISS (similarity search)
Streamlit (UI)
FastAPI + Uvicorn (API)
Pandas, NLTK

📝 Example Usage
💻 Streamlit Web App
User: "I'm feeling really sad today"
Bot: "I'm really sorry you're feeling sad. I'm here to listen if you'd like to share more."

💙 Disclaimer: I'm not a therapist. For serious issues, please contact a mental health professional.

🔌 FastAPI Endpoint
import requests

res = requests.post("http://localhost:8000/chat", json={"message": "I'm so excited!"})
print(res.json())
# {"response": "That's wonderful! I'm so glad to hear that!", "emotion": "joy", "confidence": 0.89}

🛡️ Safety & Ethics

Provides disclaimers on every response
Avoids storing user data without consent
Detects self-harm keywords and responds with crisis guidance
Ensures empathetic but non-clinical support

📈 Future Roadmap

 Multi-turn conversation memory
 Conversation history UI
 Voice input & output
 Multilingual support
 User feedback learning loop

🤝 Contributing

Fork this repo
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m "Add feature")
Push to branch (git push origin feature/amazing-feature)
Open a Pull Request

📄 License
This project is licensed under the MIT License — see LICENSE.
🙏 Acknowledgments

Hugging Face 🤗 for pre-trained models
Sentence Transformers team
Facebook Research for FAISS
Streamlit and FastAPI communities

Built with ❤️ to advance emotional AI applications
