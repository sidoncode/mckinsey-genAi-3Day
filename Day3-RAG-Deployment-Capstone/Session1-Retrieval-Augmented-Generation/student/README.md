# Session 1 — Student Notebook

## Retrieval-Augmented Generation (RAG)

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

- **5 Demos** — Follow along with the instructor. Run each cell and observe the outputs.
- **4 Hands-On Tasks** — Complete the TODO sections. Each task includes hints to guide you.

### Task Summary

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Build an embedding-based document search engine | Beginner |
| Task 2 | Implement a multi-strategy chunking pipeline | Intermediate |
| Task 3 | Create a query expansion and reranking system | Intermediate |
| Task 4 | Build a production RAG pipeline with evaluation | Advanced |

### Tips

- Read the hints carefully before writing code
- Run demo cells first to understand the patterns
- Embeddings are numerical representations — think of them as coordinates in meaning-space
- Better chunking = better retrieval = better answers
