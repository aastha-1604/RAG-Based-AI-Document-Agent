# 📄 RAG-Based AI Document Agent

An intelligent **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask context-aware questions about their content.

The system combines **FastAPI, Streamlit, LangChain, LangGraph, Pinecone, Groq, Sentence Transformers, and Tavily Search** to build an end-to-end AI document question-answering workflow with intelligent web-search fallback.

## 🚀 Open [http://localhost:3000](http://localhost:8501/) with your browser to see the result.


## ✨ Key Features

* 📤 **Multiple PDF Uploads** — Upload and process multiple PDF documents through the application.
* 🔎 **Semantic Document Retrieval** — Retrieves relevant document chunks using vector similarity search.
* 🧠 **RAG-Based Question Answering** — Combines retrieved document context with an LLM to generate grounded answers.
* 🆔 **Document-Specific Retrieval** — Uses document identifiers and metadata filtering to keep retrieval scoped to the relevant uploaded document.
* 🔀 **Agentic Workflow** — LangGraph manages retrieval, routing, response generation, and fallback logic.
* 🌐 **Web Search Fallback** — Tavily Search can provide external real-time information when sufficient document context is unavailable.
* ⚡ **FastAPI Backend** — REST API endpoints manage document uploads and question answering.
* 🖥️ **Streamlit Interface** — Simple interactive frontend for uploading PDFs and interacting with the AI agent.
* ☁️ **Pinecone Vector Database** — Stores document embeddings for scalable semantic retrieval.

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │    Streamlit UI      │
                    │       app.py         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │      main.py         │
                    └──────────┬───────────┘
                               │
               ┌───────────────┴───────────────┐
               │                               │
               ▼                               ▼
        PDF Upload                         User Question
               │                               │
               ▼                               ▼
        PyPDFLoader                       LangGraph
               │                               │
               ▼                               ▼
        Text Chunking              Document Retriever
               │                               │
               ▼                               ▼
    Sentence Transformers                  Pinecone
               │                               │
               ▼                               ▼
           Pinecone                    Relevant Context
                                               │
                                      ┌────────┴────────┐
                                      │                 │
                                      ▼                 ▼
                                Groq LLM          Tavily Search
                                      │            (Fallback)
                                      └────────┬────────┘
                                               ▼
                                         Final Answer
```

---

## 🛠️ Tech Stack

| Technology                | Purpose                                |
| ------------------------- | -------------------------------------- |
| **Python 3.12**           | Core programming language              |
| **FastAPI**               | Backend REST API                       |
| **Streamlit**             | Interactive frontend                   |
| **LangChain**             | RAG components and document processing |
| **LangGraph**             | Agentic workflow and routing           |
| **Pinecone**              | Vector database                        |
| **Sentence Transformers** | Document embeddings                    |
| **all-MiniLM-L6-v2**      | 384-dimensional embedding model        |
| **Groq API**              | Fast LLM inference                     |
| **Tavily Search**         | Real-time web-search fallback          |
| **PyPDFLoader**           | PDF document loading                   |
| **Uvicorn**               | ASGI server for FastAPI                |

---

## 🔄 RAG Workflow

### 1. Document Upload

The user uploads one or more PDF documents through the **Streamlit interface**.

```text
PDF
 ↓
FastAPI /upload
 ↓
PyPDFLoader
 ↓
Text Splitting
 ↓
Sentence Transformer Embeddings
 ↓
Pinecone Vector Database
```

Each document is associated with metadata/document identification so retrieval can be filtered to the appropriate document.

### 2. Question Answering

When the user asks a question:

```text
User Question
      ↓
FastAPI /ask
      ↓
LangGraph
      ↓
Pinecone Retriever
      ↓
Relevant Document Chunks
      ↓
Groq LLM
      ↓
Context-Aware Answer
```

### 3. Web Search Fallback

When sufficient information cannot be obtained from the uploaded document context, the workflow can route the query to **Tavily Search**.

```text
Question
   ↓
Document Retrieval
   ↓
Is sufficient context available?
   │
 ┌─┴──────────────┐
 │                │
YES               NO
 │                │
 ▼                ▼
Groq           Tavily Search
 │                │
 └───────┬────────┘
         ▼
    Final Answer
```

---

## 📂 Project Structure

```text
RAG-AI-Document-Agent/
│
├── data/
│   └── sample documents
│
├── src/
│   ├── loader.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── retriever.py
│   ├── rag.py
│   ├── graph.py
│   └── web_search.py
│
├── tests/
│   ├── test_loader.py
│   ├── test_pinecone.py
│   ├── test_retriever.py
│   ├── test_rag.py
│   └── test_graph.py
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd RAG-AI-Document-Agent
```

### 2. Create Virtual Environment

```bash
py -3.12 -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
TAVILY_API_KEY=your_tavily_api_key
```

> Never upload your `.env` file or API keys to GitHub.

---

## ▶️ Running the Application

### Start FastAPI Backend

```bash
uvicorn main:app --reload
```

FastAPI will run locally and its interactive API documentation can be accessed through the `/docs` endpoint.

### Start Streamlit Frontend

Open another terminal, activate the virtual environment and run:

```bash
streamlit run app.py
```

The Streamlit application will then open in your browser.

---

## 📡 API Endpoints

### `POST /upload`

Uploads PDF documents, processes their contents, generates embeddings, and stores them in Pinecone.

### `POST /ask`

Accepts the user's question, performs document retrieval, executes the LangGraph workflow, and returns the generated response.

---

## 📦 Core Dependencies

```text
fastapi
uvicorn
streamlit
python-multipart
requests
python-dotenv

langchain
langchain-community
langchain-text-splitters
langchain-huggingface
langchain-groq
langchain-pinecone

langgraph
pinecone
sentence-transformers
tavily-python
pypdf
```

---

## 🧠 Embedding & Retrieval

The application uses:

```text
Model: all-MiniLM-L6-v2
Embedding Dimension: 384
Vector Database: Pinecone
Similarity Metric: Cosine Similarity
```

Uploaded documents are split into smaller chunks before embeddings are generated. These vectors are stored in Pinecone and later retrieved according to semantic similarity with the user's query.

Document metadata enables filtered retrieval so that questions can be answered using the intended uploaded document context.

---

## 💡 Use Cases

This architecture can be extended to:

* Research paper analysis
* Academic document Q&A
* Business report analysis
* Policy and legal document exploration
* Technical documentation assistants
* Knowledge-base chatbots
* Enterprise document intelligence

---

## 🔮 Future Improvements

Potential extensions include conversation memory, source citations, richer document management, support for additional file formats, authentication, retrieval evaluation, reranking, and improved document selection for multi-document conversations.


---

⭐ **If you find this project useful, consider giving the repository a star!**
