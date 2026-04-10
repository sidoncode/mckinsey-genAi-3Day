# Session 1 — Student Notebook

## Retrieval-Augmented Generation for Consulting Knowledge

### Setup Instructions

1. Ensure Python 3.9+ is installed
2. Install required packages:
   ```bash
   pip install openai langchain langchain-openai langchain-community chromadb tiktoken
   ```
3. Set your API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
4. Open the notebook:
   ```bash
   jupyter notebook Session1_Student_RAG.ipynb
   ```

### What's Inside

- **5 Demos** — Follow along with the instructor. Run each cell to see how RAG retrieves and reasons over McKinsey consulting knowledge.
- **6 Hands-On Tasks + 2 Optional Bonus** — Complete the TODO sections to build consulting knowledge retrieval systems. Each task includes hints.

### Task Summary

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Build a SearchEngine class over a consulting knowledge corpus | Beginner |
| Task 2 | Implement a SmartChunker (strategy reports vs. analytics code vs. engagement notes) | Intermediate |
| Task 3 | Create an AdvancedRetriever with query expansion and reranking | Intermediate |
| Task 4 | Build an EvaluatedRAG system with relevance, faithfulness, and completeness metrics | Advanced |
| Task 5 | Build a MetadataFilteredRetriever for practice area and industry-filtered search | Intermediate |
| Task 6 | Create a ConversationalRAG with follow-up question handling | Intermediate |
| Task 7 (Optional) | Hybrid Search — keyword + semantic with Reciprocal Rank Fusion | Advanced |
| Task 8 (Optional) | RAG with hallucination detection and source grounding | Advanced |

### Tips

- Read the hints carefully before writing code
- Run demo cells first to understand the patterns
- Embeddings are numerical representations — think of them as coordinates in consulting-meaning-space
- Better chunking of consulting reports = better retrieval = better answers for engagement teams
