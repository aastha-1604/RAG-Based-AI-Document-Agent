from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_split_pdf(file_path, document_id):

    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split PDF into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    # Add document_id to every chunk
    for chunk in chunks:
        chunk.metadata["document_id"] = document_id

    return chunks