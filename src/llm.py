import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


def get_llm():

    model_name = os.getenv("GROQ_MODEL")

    if not model_name:
        raise ValueError("GROQ_MODEL not found in .env")

    llm = ChatGroq(
        model=model_name,
        temperature=0
    )

    return llm