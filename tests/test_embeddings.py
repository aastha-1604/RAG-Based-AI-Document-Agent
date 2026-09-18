from src.embeddings import get_embedding_model


embedding_model = get_embedding_model()

text = "Consulting, involves providing expert advice and recommendations to organizations or individuals to help them solve business problems and achieve their strategic, operational, or organizational goals. Consultants, analyze information, identify challenges, and recommend strategies to enhance efficiency and growth across industries."

vector = embedding_model.embed_query(text)

print("Vector length:", len(vector))

print("First 10 values:")
print(vector[:10])