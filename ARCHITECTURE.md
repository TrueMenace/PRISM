# System Architecture — PRISM (Personalized Retrieval-based Intelligent Study Mentor)

## 1. Overview

PRISM is a Retrieval-Augmented Generation (RAG) based intelligent learning system designed to provide **personalized explanations** from long-form textual content.

Instead of generating answers purely from a language model, the system:
- Retrieves relevant knowledge from a vector database (Qdrant)
- Adapts explanations based on a learner’s profile
- Uses an LLM only as a final reasoning and explanation layer

This design ensures factual grounding, explainability, and extensibility.

---

## 2. High-Level Architecture

The system is divided into **four logical layers**:

[ Data Ingestion ]
      ↓
[ Vector Storage (Qdrant) ]
      ↓
[ Retrieval + Agent Reasoning ]
      ↓
[ LLM Explanation Layer ]


Each layer is independent and loosely coupled.

---

## 3. Data Ingestion Layer

**Purpose:** Convert raw book content into machine-understandable knowledge.

### Steps:
1. Load text from a source file (`atomic_habits.txt`)
2. Split text into meaningful chunks
3. Generate embeddings using `SentenceTransformer`
4. Store embeddings with metadata in Qdrant

### Key Files:
- `load_book.py`
- `chunk_book.py`
- `embed_chunks.py`
- `store_in_qdrant.py`

### Why this matters:
- Enables semantic search instead of keyword matching
- Makes the system scalable to multiple books or documents

---

## 4. Vector Storage Layer (Qdrant)

**Purpose:** Store and retrieve knowledge efficiently using vector similarity.

### Responsibilities:
- Store embeddings and associated text payloads
- Perform cosine similarity search
- Return top-K relevant chunks

### Technology:
- Qdrant (Docker-based local deployment)

### Benefits:
- Fast semantic retrieval
- Database is independent of LLM
- Can be replaced by any vector DB with minimal changes

---

## 5. Retrieval & Agent Reasoning Layer

**Purpose:** Decide *what information* to give and *how to explain it*.

This layer:
- Takes a user query
- Retrieves relevant chunks from Qdrant
- Applies user personalization logic
- Constructs a structured explanation prompt

### Personalization Parameters:
- Learning level (beginner)
- Learning style (story-based)
- Learning goal (self-improvement)

### Key File:
- `agent_explain.py`

This layer acts as the **brain of the system**, separating reasoning from generation.

---

## 6. LLM Explanation Layer

**Purpose:** Convert structured prompts into natural language explanations.

### Design Choice:
- LLM is used **only after retrieval**
- Prevents hallucination
- Keeps explanations grounded in source material

### Implementation:
- Gemini 2.5 Flash (Free Tier)
- Fallback to mock LLM when API is unavailable

### Key File:
- `llm_runner.py`

This modular design allows easy replacement with:
- OpenAI
- Local LLMs
- Other cloud providers

---

## 7. Execution Flow (End-to-End)

1. User asks a question
2. Agent retrieves relevant chunks from Qdrant
3. Agent builds a personalized explanation prompt
4. LLM generates final response
5. Response is displayed to the user

---

## 8. Extensibility & Future Enhancements

The system is designed for future extensions such as:
- Multimodal explanations (audio summaries)
- Adaptive difficulty levels
- User memory and learning progress tracking
- Multiple document ingestion
- Web or mobile interface

These features can be added without changing the core architecture.

---

## 9. Ethics, Limitations & Safety

### Limitations:
- Depends on quality of source text
- LLM availability may vary (free tier limits)

### Ethical Considerations:
- No personal data stored
- Transparent knowledge sources
- Human-readable explanations
- Avoids hallucinations via retrieval grounding

---

## 10. Summary

PRISM demonstrates a clean, modular implementation of a **retrieval-augmented intelligent learning system** with clear separation of concerns, personalization logic, and responsible AI design principles.
