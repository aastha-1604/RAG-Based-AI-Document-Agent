from src.document_loader import load_and_split_pdf
from src.vectorstore import store_documents

document_id = "Casebook 4.0"

chunks = load_and_split_pdf(
    "data/Casebook 4.0.pdf",
    document_id
)

store_documents(chunks)

print("Upload complete.")