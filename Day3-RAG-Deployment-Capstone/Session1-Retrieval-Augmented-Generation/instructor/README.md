# Session 1 — Instructor Notebook

## Retrieval-Augmented Generation for Consulting Knowledge

### Teaching Notes

**Duration:** 1 hour 45 minutes (9:00 – 10:45)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 10 min | RAG architecture overview — building consulting knowledge assistants |
| Demo 1 | 10 min | Embeddings on consulting knowledge (digital transformation, PMI) |
| Demo 2 | 12 min | ChromaDB vector store with practice area metadata |
| Demo 3 | 12 min | Advanced chunking for PMI best practice guides |
| Demo 4 | 10 min | Multi-query expansion and HyDE for consulting research |
| Demo 5 | 10 min | End-to-end RAG with source citations |
| Task 1 | 10 min | SearchEngine over consulting corpus |
| Task 2 | 10 min | SmartChunker (strategy reports vs. analytics code) |
| Task 3 | 10 min | AdvancedRetriever with query expansion & reranking |
| Task 4 | 15 min | EvaluatedRAG with consulting quality metrics |
| Task 5 | 10 min | MetadataFilteredRetriever for practice area search |
| Task 6 | 10 min | ConversationalRAG with follow-up handling |
| Optional Task 7 | 10 min | Hybrid Search (keyword + semantic with RRF) |
| Optional Task 8 | 10 min | Hallucination detection and source grounding |
| Wrap-up | 6 min | Q&A and key takeaways |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and McKinsey consulting talking points
- **6 Solved Tasks + 2 Optional Bonus** — Complete solutions with step-by-step explanations

### Key Teaching Points

1. Embeddings capture semantic meaning in consulting knowledge — show how "digital transformation" and "enterprise modernization" are close in embedding space
2. Chunking consulting reports is the most underrated part of RAG — different document types (strategy reports vs. engagement notes) need different strategies
3. Query transformation can dramatically improve retrieval quality for complex consulting research questions
4. Always evaluate RAG with metrics — retrieval precision, answer faithfulness, citation accuracy are critical for partner-quality outputs

### Common Student Questions

- "Why not just put all consulting knowledge in the prompt?" — Context window limits, cost, and attention degradation
- "When should I use ChromaDB vs. FAISS vs. Pinecone?" — ChromaDB for prototyping, FAISS for speed, Pinecone for managed production
- "How do I handle documents that update?" — Discuss incremental indexing and versioning for evolving consulting knowledge
