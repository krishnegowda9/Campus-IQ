# 🎓 Campus-IQ

> An AI-powered campus knowledge assistant built with Retrieval-Augmented Generation (RAG), Hugging Face models, ChromaDB, and Gradio.

Campus-IQ is a local AI assistant that allows users to ask questions about campus-related documents and receive answers grounded in the information stored in those documents.

Instead of relying only on an LLM's pre-trained knowledge, Campus-IQ uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from PDF documents and provide that information to the language model as context.

### 🌐 Accessing the Web Application

Once you start the application locally or via Docker, open your browser and navigate to:

- **Local App URL:** [http://localhost:7860/](http://localhost:7860/)

  ### 🤖 Models Used

Campus-IQ runs completely local AI models from Hugging Face for embeddings and text generation:

| Component | Model Name | Description |
| :--- | :--- | :--- |
| **Embedding Model** | `sentence-transformers/all-MiniLM-L6-v2` | Converts document chunks and user queries into 384-dimensional dense vector representations for semantic search. |
| **Local LLM** | `google/flan-t5-base` | Seq2Seq text generation model used to synthesize answers grounded in retrieved document context. |

## 🔄 End-to-End RAG Workflow

```text
┌──────────────────────────────────────────────────────────────────┐
│                      📄 PDF DOCUMENTS                            │
└────────────────────────────────┬─────────────────────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   📄 PyMuPDF Loader    │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   ✂️ Text Chunker       │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   🧠 Embedding Model   │
                    │  (Hugging Face 384-D)  │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   🗄️ Vector Database    │
                    │    (ChromaDB Store)    │
                    └────────────┬───────────┘
                                 │
┌────────────────────────────────┴─────────────────────────────────┐
│                        👤 USER QUESTION                          │
└────────────────────────────────┬─────────────────────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   🔎 Semantic Search   │
                    │   (Cosine Similarity)  │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   🧩 Context Builder   │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │     🤖 Local LLM       │
                    │    (Hugging Face)      │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   💬 Gradio Interface  │
                    │   (Answer + Sources)   │
                    └────────────────────────┘

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

### 📂 Directory Architecture

```text
📦 Campus-IQ
├── 📄 app.py                  ──► Main UI entrypoint (Gradio application)
├── ⚙️ rag_pipeline.py         ──► End-to-end RAG workflow orchestrator
├── 🐳 Dockerfile               ──► Containerization environment specs
├── 📋 requirements.txt        ──► Core dependencies & package definitions
│
├── 📂 chunker/                ──► Text segmentation module
│   └── 📄 text_chunker.py     ──► Context-aware document splitting logic
│
├── 📂 database/               ──► Persistence & retrieval layer
│   ├── 📄 chroma_store.py     ──► Vector DB client & collection management
│   ├── 📄 ingest.py           ──► Batch document indexing pipeline
│   └── 📄 retriever.py        ──► Semantic similarity query engine
│
├── 📂 embeddings/             ──► Vector embedding generation
│   ├── 📄 embedding_model.py  ──► Hugging Face transformer model loader
│   └── 📄 embed_documents.py  ──► Batch text-to-vector encoding utilities
│
├── 📂 generator/              ──► Text generation engine
│   └── 📄 text_generator.py   ──► Local Hugging Face LLM inference interface
│
├── 📂 pdf_loader/             ──► Document ingestion utilities
│   └── 📄 pdf_loader.py       ──► High-performance PyMuPDF text parser
│
└── 📂 data/                   ──► Raw data storage
    └── 📂 pdfs/               ──► Input document directory
        └── 📄 sample.pdf      ──► Target PDF files for processing

### 🔄 How the RAG Pipeline Works

| Step | Stage | Action & Function | Output / Artifact |
| :---: | :--- | :--- | :--- |
| **01** | **PDF Ingestion** | Extracts raw text from source PDF files stored in `data/pdfs/`. | Unstructured Text |
| **02** | **Text Chunking** | Splits extracted text into uniform, semantically rich chunks for retrieval. | Text Chunks |
| **03** | **Embedding Generation** | Encodes each text chunk into a 384-dimensional dense vector via Hugging Face. | Dense Vectors (384-D) |
| **04** | **Vector Storage** | Indexes and stores vectors persistently in ChromaDB collection (`campus_iq_documents`). | Persistent Vector Store |
| **05** | **Question Embedding** | Converts incoming user queries into vector space using the same embedding model. | Query Vector |
| **06** | **Semantic Search** | Computes cosine similarity in ChromaDB to extract the top-matching document chunks. | Relevant Document Chunks |
| **07** | **Context Assembly** | Constructs a structured prompt block combining user query and retrieved context chunks. | Enriched Prompt Context |
| **08** | **Answer Generation** | Executes local Hugging Face LLM inference to synthesize a grounded response with source links. | Final Answer + Sources |



### 🛠️ Tech Stack & Ecosystem

| Layer | Technology | Purpose & Architectural Role |
| :--- | :--- | :--- |
| ![Python](https://img.shields.io/badge/Language-3776AB?style=flat-square&logo=python&logoColor=white) | **Python 3.x** | Core programming language powering the backend |
| ![HuggingFace](https://img.shields.io/badge/AI_Hub-FFD21E?style=flat-square&logo=huggingface&logoColor=black) | **Hugging Face** | Central hub for pre-trained embeddings & LLM download pipelines |
| ![SentenceTransformers](https://img.shields.io/badge/Embeddings-4B8BBE?style=flat-square&logo=python&logoColor=white) | **Sentence Transformers** | Encodes document chunks into dense 384-D vector representations |
| ![Transformers](https://img.shields.io/badge/Inference-FF6F00?style=flat-square&logo=tensorflow&logoColor=white) | **Transformers** | Executes local LLM text generation directly on hardware |
| ![ChromaDB](https://img.shields.io/badge/Vector_DB-008080?style=flat-square) | **ChromaDB** | Vector database for persistent similarity indexing & retrieval |
| ![PyMuPDF](https://img.shields.io/badge/Parser-E25A1C?style=flat-square&logo=adobeacrobatreader&logoColor=white) | **PyMuPDF** | Ultra-fast PDF text extraction and parsing engine |
| ![Gradio](https://img.shields.io/badge/Frontend-orange?style=flat-square&logo=gradio&logoColor=white) | **Gradio** | Powers the interactive web application interface |
| ![Docker](https://img.shields.io/badge/Container-2496ED?style=flat-square&logo=docker&logoColor=white) | **Docker** | Isolated container environment for multi-platform deployment |
| ![GitHub](https://img.shields.io/badge/VCS-181717?style=flat-square&logo=github&logoColor=white) | **Git & GitHub** | Source code management and repository hosting |


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

Access the Application
Open your browser and navigate to:

Application Interface: http://localhost:7860

Check the Container
docker ps

Expected port mapping:
0.0.0.0:7860->7860/tcp

### 🤗 Hugging Face Integration

Campus-IQ utilizes Hugging Face pipelines for entirely local, privacy-focused inference:

* **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2` (384-dimensional vector encoding)
* **Local LLM:** `google/flan-t5-base` (Grounded answer generation)

> **Note on Authentication:**  
> During initial startup, you may see a warning regarding *unauthenticated requests to HF Hub*. This is expected behavior for open-access public models and does **not** interrupt application execution. For high-throughput or production environments, set your `HF_TOKEN` environment variable.


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
<div align="center">

```text
 💻 ─────────────────────────────────────────────────────────────── 💻
 │                                                                 │
 │   👨‍💻 Author    : KrishneGowda KN                                │
 │   🌐 GitHub    : [github.com/krishnegowda9](https://github.com/krishnegowda9)                        │
 │   🚀 Status    : Building Open-Source AI & RAG Solutions          │
 │                                                                 │
 └─────────────────────────────────────────────────────────────────┘
<
⭐ Support
If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

