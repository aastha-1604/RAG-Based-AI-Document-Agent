import os

from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore

from src.embeddings import get_embedding_model


load_dotenv()


def get_vectorstore():

    index_name = os.getenv("PINECONE_INDEX_NAME")

    if not index_name:
        raise ValueError("PINECONE_INDEX_NAME not found in .env")

    embeddings = get_embedding_model()

    vectorstore = PineconeVectorStore(
        index_name=index_name,
        embedding=embeddings
    )

    return vectorstore

def store_documents(chunks):

    vectorstore = get_vectorstore()

    vectorstore.add_documents(chunks)

    print(f"Successfully stored {len(chunks)} chunks in Pinecone.")

    return vectorstore