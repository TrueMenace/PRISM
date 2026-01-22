from pathlib import Path
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct


def load_book(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text, min_length=40):
    raw_chunks = text.splitlines()
    chunks = []

    for chunk in raw_chunks:
        cleaned = chunk.strip()
        if len(cleaned) >= min_length:
            chunks.append(cleaned)

    return chunks


if __name__ == "__main__":
    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Load book
    current_dir = Path(__file__).resolve().parent
    book_path = current_dir.parent / "data" / "books" / "atomic_habits.txt"

    book_text = load_book(book_path)
    chunks = chunk_text(book_text)

    print(f"Total chunks: {len(chunks)}")

    # Create embeddings
    embeddings = model.encode(chunks)

    # Connect to local Qdrant
    client = QdrantClient(host="localhost", port=6333)

    collection_name = "atomic_habits_book"

    # Create / reset collection

    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=embeddings.shape[1],
                distance=Distance.COSINE
            )
        )
    else:
        print(f"ℹ️ Collection '{collection_name}' already exists")

    # Prepare points
    points = []
    for idx, (chunk, vector) in enumerate(zip(chunks, embeddings)):
        points.append(
            PointStruct(
                id=idx,
                vector=vector.tolist(),
                payload={
                    "text": chunk,
                    "source": "Atomic Habits"
                }
            )
        )

    # Upload to Qdrant
    client.upsert(
        collection_name=collection_name,
        points=points
    )

    print(f"Stored {len(points)} chunks in Qdrant collection '{collection_name}'")
