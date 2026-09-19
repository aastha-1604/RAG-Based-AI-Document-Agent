import os
import shutil
import uuid

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from src.document_loader import load_and_split_pdf
from src.vectorstore import store_documents
from src.graph import build_graph


app = FastAPI(
    title="RAG AI Document Agent"
)

graph = None


# Data expected by /ask
class QuestionRequest(BaseModel):
    question: str
    document_id: str


@app.get("/")
def home():

    return {
        "message": "RAG AI Document Agent API is running."
    }


# -------------------------
# PDF UPLOAD ENDPOINT
# -------------------------

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs(
        "data",
        exist_ok=True
    )

    # Generate unique ID for this uploaded PDF
    document_id = str(uuid.uuid4())

    # Store PDF using unique ID
    file_path = os.path.join(
        "data",
        f"{document_id}_{file.filename}"
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Pass document_id to loader
    chunks = load_and_split_pdf(
        file_path,
        document_id
    )

    # Store chunks + metadata in Pinecone
    store_documents(chunks)

    return {
        "message": "PDF uploaded successfully.",
        "document_id": document_id,
        "filename": file.filename,
        "chunks": len(chunks)
    }


# -------------------------
# QUESTION ENDPOINT
# -------------------------

@app.post("/ask")
def ask_question(request: QuestionRequest):
    global graph

    if graph is None:
        graph = build_graph()

    result = graph.invoke(
        {
            "question": request.question,

            # Pass ID through LangGraph
            "document_id": request.document_id,

            "answer": "",
            "source": ""
        }
    )

    return {
        "answer": result["answer"],
        "source": result["source"]
    }