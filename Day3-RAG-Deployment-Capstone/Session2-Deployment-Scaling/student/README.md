# Session 2 — Student Notebook

## Deployment and Scaling

### Setup Instructions

1. Ensure Python 3.9+ is installed
2. Install required packages:
   ```bash
   pip install openai langchain langchain-openai pandas matplotlib
   ```
3. Set your API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
4. Open the notebook:
   ```bash
   jupyter notebook Session2_Student_Deployment_Scaling.ipynb
   ```

### What's Inside

- **5 Demos** — Follow along with the instructor. Run each cell and observe the outputs.
- **4 Hands-On Tasks** — Complete the TODO sections. Each task includes hints to guide you.

### Task Summary

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Build a cached LLM API endpoint | Beginner |
| Task 2 | Implement cost tracking and budget system | Intermediate |
| Task 3 | Create a monitoring dashboard for LLM metrics | Intermediate |
| Task 4 | Design a production deployment architecture | Advanced |

### Tips

- Think about cost from the start — LLM calls add up fast
- Caching is the single biggest cost optimization for most applications
- Monitor everything: latency, token usage, error rates, and user satisfaction
- At the end of this session, you will choose your capstone track (A or B) for Session 3
