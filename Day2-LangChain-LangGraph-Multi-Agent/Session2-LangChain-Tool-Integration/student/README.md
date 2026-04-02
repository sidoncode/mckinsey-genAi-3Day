# Session 2 — Student Notebook

## LangChain Development & Tool Integration

### Setup Instructions

1. Ensure Python 3.9+ is installed
2. Install required packages:
   ```bash
   pip install langchain langchain-openai langchain-community tiktoken
   ```
3. Set your API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
4. Open the notebook:
   ```bash
   jupyter notebook Session2_Student_LangChain_Tool_Integration.ipynb
   ```

### What's Inside

- **5 Demos** — Follow along with the instructor. Run each cell and observe the outputs.
- **4 Hands-On Tasks** — Complete the TODO sections. Each task includes hints to guide you.

### Task Summary

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Build a chain with prompt templates and output parsers | Beginner |
| Task 2 | Create custom tools for math and text processing | Intermediate |
| Task 3 | Implement a conversational chain with memory | Intermediate |
| Task 4 | Build a RAG-powered Q&A system | Advanced |

### Tips

- Read the hints carefully before writing code
- Run demo cells first to understand the patterns
- Ask your instructor if you get stuck on any task
- LCEL uses the `|` (pipe) operator — think of it as Unix pipes for LLM calls
