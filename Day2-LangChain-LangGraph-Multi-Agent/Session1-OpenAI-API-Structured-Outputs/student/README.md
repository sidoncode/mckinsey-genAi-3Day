# Session 1 — Student Notebook

## OpenAI API Engineering with Structured Outputs

### Setup Instructions

1. Ensure Python 3.9+ is installed
2. Install required packages:
   ```bash
   pip install openai pydantic tiktoken
   ```
3. Set your API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
4. Open the notebook:
   ```bash
   jupyter notebook Session1_Student_OpenAI_API_Structured_Outputs.ipynb
   ```

### What's Inside

- **5 Demos** — Follow along with the instructor. Run each cell and observe how structured outputs are used for McKinsey consulting data extraction.
- **8 Hands-On Tasks** — Complete the TODO sections to build consulting AI tools. Each task includes hints to guide you.

### Task Summary

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Build a competitive intelligence extractor from M&A briefings | Beginner |
| Task 2 | Implement a financial analysis tool with function calling | Intermediate |
| Task 3 | Create a multi-tool consulting agent (market research + financial analysis + benchmarking) | Intermediate |
| Task 4 | Build a RobustConsultingClient with retries, validation, and streaming | Advanced |
| Task 5 | Parallel function calling for cross-practice research | Intermediate |
| Task 6 | Nested Pydantic models for M&A deal memo generation | Intermediate |
| Task 7 | Multi-turn tool agent with conversation memory | Advanced |
| Task 8 | Batch processing pipeline with structured validation | Advanced |

### Tips

- Read the hints carefully before writing code
- Run demo cells first to understand the patterns
- Think about how structured outputs enable downstream consulting workflows
- Each task builds on concepts from the demos — client profiles, engagement summaries, market research
