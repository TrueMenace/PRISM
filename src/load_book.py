from pathlib import Path

def load_book(file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    return text


if __name__ == "__main__":
    # Get the directory of this script (src/)
    current_dir = Path(__file__).resolve().parent

    # Build path to data/books/atomic_habits.txt
    book_path = current_dir.parent / "data" / "books" / "atomic_habits.txt"

    book_text = load_book(book_path)
    print("Book loaded successfully!")
    print("Number of characters:", len(book_text))
