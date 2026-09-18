from src.retriever import retrieve_documents


# Same document_id used while uploading to Pinecone
document_id = "Casebook 4.0"

# Test question
question = "What is consulting?"

# Retrieve relevant chunks
documents = retrieve_documents(
    question,
    document_id,
    k=4
)

print(f"\nNumber of documents retrieved: {len(documents)}")
print("\nRetrieved Documents:\n")

for i, doc in enumerate(documents, start=1):

    print(f"\n--- Document {i} ---")
    print(doc.page_content)

    print("\nMetadata:")
    print(doc.metadata)