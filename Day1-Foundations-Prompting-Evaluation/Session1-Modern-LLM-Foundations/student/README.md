# Session 1 — Student Notebook

## Modern LLM Foundations for Agentic Systems

### Setup Instructions

1. Ensure Python 3.9+ is installed
2. Install required packages from the project root:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your API key in the `.env` file at the project root:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```
4. Open the notebook:
   ```bash
   jupyter notebook Session1_Student_LLM_Foundations.ipynb
   ```

### What's Inside

- **5 Demos** — Follow along with the instructor. Run each cell and observe the outputs. All examples use McKinsey consulting scenarios.
- **8 Hands-On Tasks** — Complete the TODO sections. Each task includes hints to guide you.

### Task Summary

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Test API connection with McKinsey MECE prompt | Beginner |
| Task 2 | Optimize token usage on healthcare market research brief | Intermediate |
| Task 3 | Compare temperature settings on competitive advantage analysis | Intermediate |
| Task 4 | Build a McKinsey engagement manager agent | Intermediate |
| Task 5 | Generate and compare embeddings for semantic search | Intermediate |
| Task 6 | Build a multi-step analysis pipeline with quality review | Advanced |
| Task 7 | Estimate API costs from token usage | Intermediate |
| Task 8 | Build a context-aware routing agent | Advanced |

### Tips

- Read the hints carefully before writing code
- Run demo cells first to understand the patterns — tasks build on the same techniques
- All scenarios use McKinsey consulting context — think about how each technique applies to real engagements
- Tasks 5-8 introduce patterns (embeddings, pipelines, cost estimation, routing) that you will use extensively in Day 2 and Day 3
- The `.env` file configures model names, temperature, and max tokens — you can change these without modifying code
