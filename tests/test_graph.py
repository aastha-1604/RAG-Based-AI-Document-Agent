from src.graph import build_graph


graph = build_graph()

question = input(
    "Ask your question: "
)

result = graph.invoke(
    {
        "question": question,
        "answer": "",
        "source": ""
    }
)

print("\nAnswer:")
print(result["answer"])

print("\nSource:")
print(result["source"])