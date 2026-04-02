# Session 1 — Instructor Notebook

## Retrieval-Augmented Generation (RAG)

### Teaching Notes

**Duration:** 1 hour 45 minutes (9:00 – 10:45)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 10 min | RAG architecture overview, connection to Day 2 |
| Demo 1 | 10 min | Embedding models and similarity |
| Demo 2 | 12 min | Vector stores with ChromaDB |
| Demo 3 | 12 min | Advanced chunking strategies |
| Demo 4 | 10 min | Query transformation techniques |
| Demo 5 | 10 min | End-to-end RAG with citations |
| Task 1 | 10 min | Embedding-based search |
| Task 2 | 10 min | Multi-strategy chunking |
| Task 3 | 10 min | Query expansion & reranking |
| Task 4 | 15 min | Production RAG with evaluation |
| Wrap-up | 6 min | Q&A and key takeaways |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and talking points
- **4 Solved Tasks** — Complete solutions with step-by-step explanations

### Key Teaching Points

1. Embeddings capture semantic meaning — show how "dog" and "puppy" are close in embedding space
2. Chunking is the most underrated part of RAG — garbage in, garbage out
3. Query transformation can dramatically improve retrieval quality for complex questions
4. Always evaluate RAG with metrics — retrieval precision, answer faithfulness, citation accuracy

### Common Student Questions

- "Why not just put everything in the prompt?" — Context window limits, cost, and attention degradation
- "When should I use ChromaDB vs. FAISS vs. Pinecone?" — ChromaDB for prototyping, FAISS for speed, Pinecone for managed production
- "How do I handle documents that update?" — Discuss incremental indexing and versioning strategies
