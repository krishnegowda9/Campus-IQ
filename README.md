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

### 🔄 How the RAG Pipeline Works
1. **PDF Ingestion:** Extracts text from documents stored in `data/pdfs/`.
2. **Text Chunking:** Splits extracted text into smaller, manageable chunks for fast retrieval.
3. **Embedding Generation:** Converts each chunk into a 384-dimensional vector representation using a Hugging Face model.
4. **Vector Storage:** Stores embeddings and text chunks persistently in the `campus_iq_documents` ChromaDB collection.
5. **Question Embedding:** Embeds the incoming user query using the same embedding model.
6. **Semantic Search:** Performs cosine similarity search in ChromaDB to retrieve the most relevant text chunks.
7. **Context Assembly:** Combines the top retrieved chunks into a prompt context block.
8. **Answer Generation:** Runs the local Hugging Face model to synthesize a final answer grounded in the retrieved context.

### 🛠️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **Hugging Face** | AI model ecosystem |
| **Sentence Transformers** | Dense vector embeddings |
| **Transformers** | Local text generation inference |
| **ChromaDB** | Vector database for similarity search |
| **PyMuPDF** | High-performance PDF text extraction |
| **Gradio** | Interactive web UI framework |
| **Docker** | Containerization and environment isolation |
| **Git** | Distributed version control |
| **GitHub** | Source code hosting and repository management |

### 🚀 Quick Start (Local Setup)

1. **Clone the repository**
   ```bash
   git clone [https://github.com/krishnegowda9/Campus-IQ.git](https://github.com/krishnegowda9/Campus-IQ.git)
   cd Campus-IQ

2.Create and activate a virtual environment

Bash
# Create environment
python -m venv .venv

3.Install dependencies

Bash
pip install -r requirements.txt

4.Add and ingest documents
Place your PDF files in data/pdfs/ and run the ingestion pipeline:
python -m database.ingest
Ingestion Flow: PDF ──► Text Extraction ──► Chunking ──► Embedding Generation ──► ChromaDB

5.Start the application
python app.py

Access the web interface at http://localhost:7860.



🐳 Run with Docker
Campus-IQ can also be run as a Docker container
Build the Image
docker build -t campus-iq .

Run the Container
docker run -p 7860:7860 campus-iq

Open the application:
http://localhost:7860

Check the Container
docker ps

Expected port mapping:
0.0.0.0:7860->7860/tcp

🤗 Hugging Face
Campus-IQ uses Hugging Face models for embeddings and local text generation.

During startup you may see:
Warning: You are sending unauthenticated requests to the HF Hub.
This is a warning and does not necessarily mean the application has failed.

Authentication can provide higher Hugging Face Hub rate limits.

For production usage, configure your Hugging Face token securely.

⚠️ Never commit your Hugging Face token to GitHub.


💡 Example Questions
Once the required documents are loaded, users can ask questions such as:
What is Docker?

What is containerization?

What is a Dockerfile?

What is Docker Compose?

What is a Docker Volume?

What is the difference between Docker and a virtual machine?

Why are containers lightweight?

How does Docker work?


📌 Current Status
Completed
 PDF loading
 PDF text extraction
 Text chunking
 Embedding generation
 ChromaDB integration
 Semantic search
 Document retrieval
 Local text generation
 RAG pipeline
 Gradio interface
 Docker containerization
 Hugging Face model caching
 Git repository
 GitHub repository


📦 Main Components
app.py
Starts the Gradio web application.

rag_pipeline.py
Connects the retrieval and generation components together.

pdf_loader/pdf_loader.py
Loads and extracts text from PDF documents.

chunker/text_chunker.py
Splits extracted text into manageable chunks.

embeddings/embedding_model.py
Loads the embedding model.

embeddings/embed_documents.py
Creates embeddings for document chunks.

database/chroma_store.py
Stores and searches document embeddings using ChromaDB.

database/ingest.py
Handles document ingestion into the vector database.

database/retriever.py
Handles document retrieval.

generator/text_generator.py
Loads the local Hugging Face text-generation model.

Dockerfile
Defines the Docker environment used to run Campus-IQ.


🌟 Project Goal
The goal of Campus-IQ is to demonstrate how modern AI systems can combine:
Documents
   +
Embeddings
   +
Vector Database
   +
Semantic Search
   +
Local Language Model
   =
Retrieval-Augmented AI Assistant
Campus-IQ is designed as a practical implementation of a local RAG-based knowledge assistant.

👨‍💻 Author
KrishneGowda KN

GitHub:

https://github.com/krishnegowda9

⭐ Support
If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

