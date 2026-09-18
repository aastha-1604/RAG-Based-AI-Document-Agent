from src.document_loader import load_and_split_pdf

document_id = "test-document-001"

chunks = load_and_split_pdf(
    "data/Casebook 4.0.pdf",
    document_id
)

print("\nNumber of chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0].page_content)

print("\nMetadata:")
print(chunks[0].metadata)