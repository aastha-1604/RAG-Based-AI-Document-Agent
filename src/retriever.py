from src.vectorstore import get_vectorstore


def retrieve_documents(query, document_id, k=4):

    vectorstore = get_vectorstore()

    documents = vectorstore.similarity_search(
        query,
        k=k,
        filter={"document_id": document_id}
    )

    return documents