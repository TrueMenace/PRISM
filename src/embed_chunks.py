from pathlib import Path
from sentence_transformers import SentenceTransformer

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

    print(f"Embedding shape: {embeddings.shape}")
    print("Sample embedding (first 5 values):")
    print(embeddings[0][:5])
