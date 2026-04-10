# Session 1: Retrieval-Augmented Generation for Consulting Knowledge

**Time:** 9:00 – 10:45 (1 hour 45 minutes) | **Shared session — all participants**

## Overview

This session takes RAG from the simple keyword-matching demo in Day 2 to a production-grade pipeline built on McKinsey consulting knowledge. Participants will learn embedding-based retrieval over consulting documents, vector stores with practice area metadata, advanced chunking strategies for consulting reports, query transformation for research questions, and reranking — the techniques that make consulting knowledge assistants reliable.

## Key Topics

- Embedding models applied to consulting knowledge (digital transformation, PMI, supply chain)
- Vector stores (ChromaDB) with McKinsey practice area metadata
- Advanced chunking strategies for consulting reports (PMI best practices, engagement playbooks)
- Query transformation (HyDE, multi-query expansion) for consulting research
- End-to-end RAG pipeline with source citations from engagement playbooks

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session1_Student_RAG.ipynb` | 5 guided demos + 6 TODO exercises + 2 optional bonus tasks |
| `instructor/Session1_Instructor_RAG.ipynb` | 5 fully solved demos + 8 exercises with explanations |

## Demos (5)

1. **Demo 1:** Embeddings on consulting knowledge — digital transformation, PMI, omnichannel, supply chain
2. **Demo 2:** ChromaDB vector store — "mckinsey_knowledge_base" collection with practice area metadata
3. **Demo 3:** Advanced chunking of PMI best practice guides
4. **Demo 4:** Multi-query expansion and HyDE for consulting research questions
5. **Demo 5:** End-to-end RAG with source citations from engagement playbooks

## Exercises (6 + 2 Optional)

1. **Task 1:** Build a SearchEngine class over a consulting knowledge corpus
2. **Task 2:** Implement a SmartChunker that detects strategy reports, analytics code, and engagement notes
3. **Task 3:** Create an AdvancedRetriever with query expansion and reranking
4. **Task 4:** Build an EvaluatedRAG system with relevance, faithfulness, and completeness metrics
5. **Task 5:** Build a MetadataFilteredRetriever for practice area and industry-filtered search
6. **Task 6:** Create a ConversationalRAG with follow-up question rewriting and multi-turn memory

### Optional / Bonus

7. **Task 7 (Optional):** Hybrid Search — combining keyword (BM25-style) and semantic retrieval with Reciprocal Rank Fusion
8. **Task 8 (Optional):** RAG with hallucination detection — verify every claim is grounded in retrieved sources
