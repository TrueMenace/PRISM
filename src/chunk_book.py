from pathlib import Path

def load_book(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text, min_length=40):

    """
    Splits text into chunks based on paragraphs.
    Filters out very short chunks.
    """
    raw_chunks = text.splitlines()

    chunks = []

    for chunk in raw_chunks:
        cleaned = chunk.strip()
        if len(cleaned) >= min_length:
            chunks.append(cleaned)

    return chunks


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    book_path = current_dir.parent / "data" / "books" / "atomic_habits.txt"

    book_text = load_book(book_path)
    chunks = chunk_text(book_text)

    print(f"Total chunks created: {len(chunks)}\n")

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:")
        print(chunk[:200], "...\n")
