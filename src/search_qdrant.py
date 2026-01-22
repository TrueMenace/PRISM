from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient


if __name__ == "__main__":
    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Connect to Qdrant
    client = QdrantClient(host="localhost", port=6333)

    collection_name = "atomic_habits_book"

    # User query
    query = "How do habits become part of identity?"

    # Convert query to embedding
    query_vector = model.encode(query).tolist()

    # Search Qdrant (NEW API)
    results = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=3
    ).points

    print(f"\nQuery: {query}\n")
    print("Top matching chunks:\n")

    for i, result in enumerate(results):
        print(f"Result {i + 1} (score: {result.score:.4f}):")
        print(result.payload["text"])
        print("-" * 50)
