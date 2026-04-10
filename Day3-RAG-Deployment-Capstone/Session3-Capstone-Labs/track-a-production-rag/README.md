# Session 3 — Capstone Track A: McKinsey Knowledge Assistant (Production RAG)

**Time:** 1:30 – 3:15 (1 hour 45 minutes) | **Parallel session — Track A participants only**

## Overview

In this capstone lab, you will build a complete McKinsey Knowledge Assistant — a production-grade RAG service over a consulting document corpus. Starting with raw consulting documents, you will implement the full pipeline: intelligent chunking with practice area detection, embedding and indexing with metadata, multi-strategy retrieval, MECE-structured answer generation with citations, and consulting-specific quality evaluation.

## Capstone Project

Build a **McKinsey Knowledge Assistant** that:
1. Ingests and chunks a corpus of consulting documents with practice area metadata
2. Embeds and indexes chunks in a vector store with consulting-specific metadata
3. Retrieves relevant context using hybrid search (semantic + keyword)
4. Generates MECE-structured answers with source citations
5. Evaluates answer quality with consulting-specific metrics (strategic relevance, faithfulness, executive readiness)

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session3_Student_Track_A_Production_RAG.ipynb` | Guided capstone with TODO milestones |
| `instructor/Session3_Instructor_Track_A_Production_RAG.ipynb` | Fully solved capstone with explanations |

## Milestones (6)

1. **Milestone 1:** Consulting document ingestion and intelligent chunking pipeline with practice area detection
2. **Milestone 2:** Embedding, indexing, and hybrid retrieval over McKinsey knowledge base
3. **Milestone 3:** MECE-structured answer generation with source citations
4. **Milestone 4:** Consulting-specific evaluation pipeline (strategic relevance, faithfulness, executive readiness)
5. **Milestone 5:** Multi-turn conversational knowledge assistant with follow-up question rewriting
6. **Milestone 6:** A/B testing and configuration comparison to optimize RAG pipeline settings
