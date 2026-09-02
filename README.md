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

