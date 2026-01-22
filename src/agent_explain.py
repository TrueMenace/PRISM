from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# -----------------------------
# Configuration
# -----------------------------
COLLECTION_NAME = "atomic_habits_book"
MODEL_NAME = "all-MiniLM-L6-v2"

# -----------------------------
# User Profile (USP)
# -----------------------------
user_profile = {
    "level": "beginner",
    "learning_style": "story",
    "goal": "self improvement"
}

# -----------------------------
# Initialize clients (REST only)
# -----------------------------
client = QdrantClient(
    url="http://localhost:6333",
    prefer_grpc=False
)

embedder = SentenceTransformer(MODEL_NAME)

# -----------------------------
# Agent Logic
# -----------------------------
def explain(query: str):
    query_vector = embedder.encode(query).tolist()

    # ✅ CORRECT QDRANT API (v1.16+)
    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3
    )

    results = search_result.points

    retrieved_text = "\n".join(
        hit.payload["text"] for hit in results
    )

    explanation_prompt = f"""
You are an AI learning assistant.

User profile:
- Level: {user_profile['level']}
- Learning style: {user_profile['learning_style']}
- Goal: {user_profile['goal']}

Context:
{retrieved_text}

Now explain the concept in a {user_profile['learning_style']} style,
appropriate for a {user_profile['level']} learner.
"""

    return explanation_prompt

# -----------------------------
# Run Agent
# -----------------------------
if __name__ == "__main__":
    query = "How do habits become part of identity?"
    output = explain(query)

    print("===== AGENT PROMPT OUTPUT =====\n")
    print(output)
