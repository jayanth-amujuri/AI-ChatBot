# 🤖 Coding Club Chatbot

An AI-powered chatbot built with Streamlit, LangChain, FAISS, and Ollama to answer questions about your college **Coding Club**, including events, registration details, and activities.

---

## 🚀 Features

- **Local Language Model**: Powered by Ollama running LLaMA 3 (or any local model)
- **Context-aware Q&A**: Uses `club_info.txt` as the knowledge base
- **Embeddings**: Uses `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Store**: FAISS for efficient similarity search
- **Interactive Chat UI**: Built with Streamlit’s new `chat_input()` and `chat_message()`

---

## 🛠️ Tech Stack

| Component        | Technology                             |
|------------------|-----------------------------------------|
| Frontend         | Streamlit (chat interface)              |
| Backend          | Python + LangChain                      |
| Embeddings       | HuggingFace: `all-MiniLM-L6-v2`         |
| Vector DB        | FAISS                                   |
| LLM              | Ollama (local LLaMA model)              |

---

## 📁 Project Structure


chatbot/
│
├── club_info.txt # Knowledge base (your club info)
├── chatbot.py # Main chatbot app (Streamlit + LangChain)
|── ollama.py #For testing the ollamma is installed or not
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## 📦 Setup Instructions

### 1. Install Python dependencies

-- pip install -r requirements.txt

-- ollama run llama3

-- streamlit run chatbot.py


📄 Example Prompts
“What is the Coding Club?”

“How do I register for the next hackathon?”

“Tell me about recent events.”

🙋‍♂️ Author
Amujuri Jayanthkumar
B.Tech in AI & Data Science | SRKR Engineering College














