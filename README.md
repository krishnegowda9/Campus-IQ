🎓 Campus-IQ

An AI-powered campus knowledge assistant built with Retrieval-Augmented Generation (RAG), Hugging Face models, ChromaDB, and Gradio.

Campus-IQ is a local AI assistant that allows users to ask questions about campus-related documents and receive answers grounded in the information stored in those documents.

Instead of relying only on an LLM's pre-trained knowledge, Campus-IQ uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded PDF documents and provide that information to the language model as context.

✨ Features
📄 PDF document ingestion
✂️ Automatic text chunking
🧠 Hugging Face embeddings
🔎 Semantic document retrieval
🗄️ Persistent ChromaDB vector database
🤖 Local Hugging Face text generation model
🔗 Retrieval-Augmented Generation (RAG) pipeline
💬 Interactive Gradio interface
🐳 Docker support
💾 Local model caching
📚 Retrieved source display
🔒 Runs locally without requiring an external LLM API
🏗️ Architecture
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
                    │  Hugging Face LLM   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Final Answer     │
                    └─────────────────────┘

🔄 RAG Pipeline

Campus-IQ follows a simple Retrieval-Augmented Generation workflow:

1. Document ingestion

PDF documents are loaded from:

data/pdfs/


The PDF text is extracted and divided into smaller chunks.

2. Embedding generation

Each document chunk is converted into a numerical vector using a Hugging Face embedding model.

The current embedding size is:

384 dimensions

3. Vector storage

The generated embeddings and document chunks are stored in a persistent ChromaDB collection.

campus_iq_documents

4. Question retrieval

When a user asks a question, the question is converted into an embedding.

Campus-IQ then searches ChromaDB for the most relevant document chunks.

5. Context construction

The retrieved documents are combined into a context passed to the text generation model.

6. Answer generation

The local Hugging Face text model generates an answer based on the retrieved context.

📂 Project Structure
Campus-IQ/
│
├── app.py
├── rag_pipeline.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
│
├── chunker/
│   ├── __init__.py
│   └── text_chunker.py
│
├── database/
│   ├── chroma_store.py
│   ├── ingest.py
│   └── retriever.py
│
├── embeddings/
│   ├── __init__.py
│   ├── embedding_model.py
│   └── embed_documents.py
│
├── generator/
│   └── text_generator.py
│
├── pdf_loader/
│   └── pdf_loader.py
│
└── data/
    └── pdfs/
        └── Docker 1.pdf

🛠️ Technology Stack
Technology	Purpose
Python	Core programming language
Hugging Face	Embeddings and local text generation
Sentence Transformers	Text embeddings
ChromaDB	Vector database
PyMuPDF	PDF text extraction
Gradio	Web interface
Transformers	Local model inference
Docker	Containerization
Git & GitHub	Version control
🚀 Running Locally
1. Clone the repository
git clone https://github.com/krishnegowda9/Campus-IQ.git
cd Campus-IQ

2. Create a virtual environment

Windows:

python -m venv .venv


Activate it:

.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Ingest documents

Place PDF files inside:

data/pdfs/


Then run:

python -m database.ingest


This extracts the PDF text, creates chunks, generates embeddings, and stores them in ChromaDB.

5. Start Campus-IQ
python app.py


The Gradio interface will be available at:

http://localhost:7860

🐳 Running with Docker

Campus-IQ can also run inside a Docker container.

Build the image
docker build -t campus-iq .

Run the container
docker run -p 7860:7860 campus-iq


Then open:

http://localhost:7860

Check the running container
docker ps


You should see port mapping similar to:

0.0.0.0:7860->7860/tcp

🤗 Hugging Face Authentication

Campus-IQ can download models from the Hugging Face Hub.

Without authentication, you may see:

Warning: You are sending unauthenticated requests to the HF Hub.


This is not necessarily an application error. Authentication can provide higher Hub rate limits and improve model downloads.

For production or shared deployments, configure your Hugging Face token securely rather than committing it to Git.

Never commit your HF token to GitHub.

💡 Example Questions

After loading the relevant documents, users can ask questions such as:

What is Docker?

What is containerization?

What is a Dockerfile?

What is Docker Compose?

What is a Docker Volume?

What is the difference between Docker and a virtual machine?

Why do containers start faster than virtual machines?


Campus-IQ retrieves relevant document chunks and uses them as context for generating the response.

🔍 Why RAG?

Traditional language models answer questions using their pre-trained knowledge.

RAG adds an external knowledge layer:

User Question
      ↓
Retrieve relevant information
      ↓
Provide information to the model
      ↓
Generate grounded answer


This makes it possible to build assistants that answer questions using specific private or domain-specific documents instead of relying entirely on general model knowledge.

📌 Current Status

Campus-IQ is currently a working prototype.

Completed
 PDF loading
 Text extraction
 Text chunking
 Embedding generation
 ChromaDB integration
 Semantic retrieval
 Local text generation
 RAG pipeline
 Gradio interface
 Docker containerization
 Git/GitHub integration
 Local Hugging Face model caching
Future Improvements
 Multi-PDF document management
 Document upload directly through the UI
 Better source citations
 Conversation memory
 Improved answer evaluation
 Authentication and user management
 Production deployment
 Docker Hub publishing
 Automated CI/CD
 Improved model performance and latency
⚠️ Notes

Campus-IQ currently runs local Hugging Face models, so the initial startup can take some time depending on the machine's CPU, RAM, storage speed, and whether the models are already cached.

The Docker image may also be large because it contains Python dependencies and machine-learning model files.

👨‍💻 Author

Krishnegowda

GitHub:

https://github.com/krishnegowda9

⭐ Project

If you find Campus-IQ useful or interesting, consider giving the repository a ⭐ on GitHub.

Campus-IQ — Turning campus documents into an intelligent, searchable knowledge assistant.
