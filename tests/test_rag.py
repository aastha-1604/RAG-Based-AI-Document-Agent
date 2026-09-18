from src.rag import answer_from_document


question = input("Ask your question: ")

answer = answer_from_document(question)

print("\nAnswer:")
print(answer)