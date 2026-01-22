# PRISM — Personalized Retrieval-based Intelligent Study Mentor

PRISM is an AI-powered learning system that helps users **understand knowledge from books and long-form content without reading everything themselves**.

The system retrieves relevant information from stored knowledge and generates **personalized explanations** based on the user’s learning style and level.

This project is built as a **real system**, not a demo, and demonstrates retrieval, memory, and reasoning using Qdrant and a modern LLM.

---

## 🚩 Problem Statement

Many people want to learn from books but struggle with:
- Lack of reading habits
- Time constraints
- Different learning preferences

Books contain valuable knowledge, but the format is not always accessible to everyone.

**PRISM addresses this by:**
- Extracting knowledge from books
- Storing it in a searchable memory
- Explaining concepts in a personalized way using AI

---

## 💡 Solution Overview

PRISM uses a **Retrieval-Augmented Generation (RAG)** approach:

1. Book content is stored as semantic embeddings
2. Relevant knowledge is retrieved based on the user query
3. An AI agent builds a personalized explanation prompt
4. A language model generates a human-friendly explanation

This ensures answers are **grounded in real content**, not hallucinated.

---

## 🧠 System Architecture

The system is divided into the following layers:

- **Data Ingestion**: Load, chunk, and embed book text
- **Vector Memory**: Store embeddings in Qdrant
- **Retrieval & Agent Reasoning**: Fetch relevant context and personalize explanations
- **LLM Generation**: Generate natural language explanations

Detailed architecture is documented in [`ARCHITECTURE.md`](ARCHITECTURE.md).

---

## 🧩 Key Technologies

- **Python**
- **Qdrant** — Vector database for semantic search and memory
- **SentenceTransformers** — Text embeddings
- **Gemini 2.5 Flash** — Language model (free tier)
- **Docker** — Running Qdrant locally

---

## 🧠 Why Qdrant is Critical

Qdrant is the backbone of PRISM’s memory system.

It enables:
- Semantic search over book knowledge
- Fast retrieval of relevant concepts
- Separation of memory from reasoning
- Scalable, production-like architecture

Without Qdrant, the system would degrade into a simple prompt-based chatbot.

---

## 📂 Project Structure

prism/
│── src/
│ ├── load_book.py
│ ├── chunk_book.py
│ ├── embed_chunks.py
│ ├── store_in_qdrant.py
│ ├── search_qdrant.py
│ ├── agent_explain.py
│ └── llm_runner.py
│
│── data/
│ └── books/
│ └── atomic_habits.txt
│
│── ARCHITECTURE.md
│── README.md
│── requirements.txt
│── .gitignore


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd prism
```

2️⃣ Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Start Qdrant (Docker)
```bash
docker run -d -p 6333:6333 qdrant/qdrant
```

Open dashboard:
```bash
http://localhost:6333/dashboard
```

🔐 Environment Variables
Create a .env file in the project root:
```ini
GEMINI_API_KEY=your_api_key_here
```
Ensure .env is added to .gitignore

▶️ Running the System
Load data into Qdrant
```bash
python src/store_in_qdrant.py
```

Run the AI Tutor
```bash
python src/llm_runner.py
```

🧪 Example Query
```rust
How do habits become part of identity?
```
The system retrieves relevant book content and explains it in a story-based style for beginners.

⚠️ Limitations & Ethics

Limitations
- Depends on quality of source text
- Free-tier LLM availability may vary

Ethics
- No personal user data stored
- Transparent retrieval-based explanations
- Reduced hallucinations via grounding

🚀 Future Enhancements
- Audio-based explanations
- Adaptive difficulty levels
- User learning progress memory
- Multi-book support
- Web or mobile interface

📌 Summary
- PRISM demonstrates a complete AI system combining:
- Vector memory
- Semantic search
- Agent-based reasoning
- LLM-powered explanations
- It is designed to be extensible, explainable, and aligned with real-world AI system principles.