from src.retriever import retrieve_documents
from src.llm import get_llm
def answer_from_document(question, document_id):

    documents = retrieve_documents(
        question,
        document_id,
        k=4
    )

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = f"""
You are an AI document assistant.

Answer the user's question using ONLY the
provided document context.

If the answer cannot be found in the context,
respond exactly with:

INSUFFICIENT_CONTEXT

Document Context:
{context}

Question:
{question}

Answer:
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content