# 🎓 Campus-IQ

> An AI-powered campus knowledge assistant built with Retrieval-Augmented Generation (RAG), Hugging Face models, ChromaDB, and Gradio.

Campus-IQ is a local AI assistant that allows users to ask questions about campus-related documents and receive answers grounded in the information stored in those documents.

Instead of relying only on an LLM's pre-trained knowledge, Campus-IQ uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from PDF documents and provide that information to the language model as context.

---

## ✨ Features

- 📄 PDF document ingestion
- ✂️ Automatic text chunking
- 🧠 Hugging Face embeddings
- 🔎 Semantic document retrieval
- 🗄️ Persistent ChromaDB vector database
- 🤖 Local Hugging Face text generation model
- 🔗 Retrieval-Augmented Generation (RAG) pipeline
- 💬 Interactive Gradio interface
- 🐳 Docker support
- 💾 Local Hugging Face model caching
- 📚 Retrieved source display
- 🔒 Runs locally without requiring an external LLM API

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      User Query     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Question Embedding │
                    │  Hugging Face Model │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      ChromaDB       │
                    │ Semantic Retrieval  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Retrieved Documents │
                    │      / Context      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Local Text Model  │
                    │  Hugging Face Model │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Final Answer     │
                    └─────────────────────┘

🔄 RAG Pipeline
Campus-IQ follows a Retrieval-Augmented Generation workflow.

1. Document Ingestion
PDF documents are loaded from:

data/pdfs/

The PDF text is extracted and divided into smaller chunks.

2. Embedding Generation
Each document chunk is converted into a numerical vector using a Hugging Face embedding model.

Current embedding size:

384 dimensions

3. Vector Storage
The generated embeddings and document chunks are stored in a persistent ChromaDB collection.

campus_iq_documents

4. Question Retrieval
When a user asks a question, the question is converted into an embedding.

Campus-IQ searches ChromaDB for the most relevant document chunks.

5. Context Construction
The retrieved documents are combined into a context that is passed to the local text generation model.

6. Answer Generation
The local Hugging Face model generates an answer using the retrieved context.

## 📂 Project Structure

```text
Campus-IQ/
├── app.py                  # Main Gradio application entry point
├── rag_pipeline.py          # Core RAG orchestration pipeline
├── Dockerfile               # Container build configuration
├── requirements.txt         # Python dependency specifications
│
├── chunker/                 # Text splitting logic
│   └── text_chunker.py
├── database/                # Vector store setup, ingestion & retrieval
│   ├── chroma_store.py
│   ├── ingest.py
│   └── retriever.py
├── embeddings/              # Embedding model wrappers & batch generation
│   ├── embedding_model.py
│   └── embed_documents.py
├── generator/               # Local Hugging Face LLM inference module
│   └── text_generator.py
├── pdf_loader/              # PDF parsing utilities
│   └── pdf_loader.py
└── data/                    # Document directory
    └── pdfs/                # Source PDFs for ingestion

Component,Technology
Language,Python 3.x
Embeddings,Hugging Face / Sentence Transformers
Vector DB,ChromaDB
PDF Processing,PyMuPDF
User Interface,Gradio
Inference,Hugging Face Transformers
Containerization,Docker
🚀 Quick Start
Option 1: Running Locally
Clone the repository

Bash
git clone [https://github.com/krishnegowda9/Campus-IQ.git](https://github.com/krishnegowda9/Campus-IQ.git)
cd Campus-IQ
Set up virtual environment

Bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
Install dependencies

Bash
pip install -r requirements.txt
Ingest Documents
Place your PDF files inside data/pdfs/ and run the ingestion pipeline:

Bash
python -m database.ingest
Launch the application

Bash
python app.py
Access the app at http://localhost:7860.

Option 2: Running with Docker
Build image

Bash
docker build -t campus-iq .
Run container

Bash
docker run -p 7860:7860 campus-iq
Open http://localhost:7860 in your browser.

🔑 Hugging Face Token Configuration (Optional)
To avoid rate limiting warnings when downloading large models from Hugging Face Hub:

Bash
export HF_TOKEN="your_hugging_face_token"
⚠️ Note: Never commit your secret tokens or API keys to git repository files.

📌 Roadmap
[x] Core RAG pipeline with local Hugging Face model & ChromaDB

[x] Gradio UI & Docker support

[ ] Direct PDF file upload from the web interface

[ ] Multi-document collection filter & management

[ ] Source citation highlights in generated responses

[ ] Conversation memory for multi-turn chats

👨‍💻 Author
Developed by Krishnegowda K N. Show your support by dropping a ⭐ if you find this project helpful!
