from src.llm import get_llm


llm = get_llm()

response = llm.invoke(
    "Explain Porter's 5 forces."
)

print(response.content) 