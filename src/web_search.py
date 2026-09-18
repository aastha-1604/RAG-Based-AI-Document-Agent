from src.llm import get_llm
import os

from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()


def search_web(query):

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError(
            "TAVILY_API_KEY not found in .env"
        )

    client = TavilyClient(
        api_key=api_key
    )

    response = client.search(
        query=query,
        max_results=5
    )

    results = response.get(
        "results",
        []
    )

    context = "\n\n".join(
        result.get("content", "")
        for result in results
    )

    return context

def answer_from_web(question):

    # The question is passed to search_web()
    context = search_web(question)

    prompt = f"""
    Answer the question using the web search context.

    Web Context:
    {context}

    Question:
    {question}

    Answer:
    """

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content 