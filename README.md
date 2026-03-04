# 📄 AI PDF Assistant using RAG and ChromaDB

An AI-powered PDF Question Answering system built using Retrieval Augmented Generation (RAG), ChromaDB, Sentence Transformers, and Streamlit.

This application allows users to upload any PDF and ask questions based on its content.

---

## 🚀 Features

- 📂 Upload any PDF file
- ✂️ Automatic text extraction from PDF
- 🧠 Semantic chunk embedding using Sentence Transformers
- 🗄 Vector storage using ChromaDB
- 🔎 Similarity-based retrieval
- 💬 Question answering from uploaded document
- 🌐 Streamlit web interface

---

## 🛠 Tech Stack

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- PyPDF

---

## 📁 Project Structure


RAG_Project
│
├── app.py # Streamlit UI
├── pdf_utils.py # PDF text extraction
├── main.py # Basic RAG script
├── requirements.txt
├── README.md
├── .gitignore
└── data/


---

## ⚙️ Installation

1. Clone the repository


git clone https://github.com/Varshakaleeswaran/RAG_Project.git

cd RAG_Project


2. Create virtual environment


python -m venv venv
venv\Scripts\activate # Windows


3. Install dependencies


pip install -r requirements.txt


---

## ▶️ Run the Application


streamlit run app.py


Open browser at:


http://localhost:8501


---

## 🧠 How It Works

1. User uploads a PDF
2. Text is extracted using PyPDF
3. Text is split into chunks
4. Each chunk is converted into embeddings
5. Embeddings are stored in ChromaDB
6. User asks a question
7. Query is embedded and matched with similar chunks
8. Most relevant content is returned as answer

---

## 🎯 Use Cases

- 📚 Academic Notes Assistant
- 📄 Research Paper Analyzer
- 🤖 Technical Documentation Assistant
- 📑 Legal Document Search
- 📊 Company Policy QA System

---

## 📌 Future Improvements

- Persistent ChromaDB storage
- OpenAI/GPT-based answer generation
- Chat history memory
- Multi-PDF support
- Deployment on Streamlit Cloud

---

## 👩‍💻 Author

**Varsha Kaleeswaran**

---

## ⭐ If you like this project

Give it a star on GitHub!