import os
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
pinecone_key = os.getenv("PINECONE_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

print("Groq:", bool(groq_key))
print("Pinecone:", bool(pinecone_key))
print("Tavily:", bool(tavily_key))