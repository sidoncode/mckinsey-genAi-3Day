# Session 4 — Student Notebook

## Multi-Agent Workflows & Agentic Systems

### Setup Instructions

1. Ensure Python 3.9+ is installed
2. Install required packages:
   ```bash
   pip install langgraph langchain langchain-openai
   ```
3. Set your API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
4. Open the notebook:
   ```bash
   jupyter notebook Session4_Student_Multi_Agent_Workflows.ipynb
   ```

### What's Inside

- **5 Demos** — Follow along with the instructor. Run each cell and observe the outputs.
- **4 Hands-On Tasks** — Complete the TODO sections. Each task includes hints to guide you.

### Task Summary

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Build a two-agent supervisor-worker system | Intermediate |
| Task 2 | Implement agent handoff with context preservation | Intermediate |
| Task 3 | Create a parallel research and synthesis pipeline | Advanced |
| Task 4 | Design and document a complete multi-agent architecture | Advanced |

### Tips

- Read the hints carefully before writing code
- Run demo cells first to understand the patterns
- Think about which parts of a problem can be parallelized vs. must be sequential
- Consider what information each agent needs from other agents
