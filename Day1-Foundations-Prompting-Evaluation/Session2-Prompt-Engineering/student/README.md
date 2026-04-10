# Session 2 — Student Notebook

## Prompt Engineering for Agentic Behaviors

### Setup Instructions

1. Ensure you have completed Session 1 setup (Python, packages, API key)
2. Install LangChain (used in Demo 6):
   ```bash
   pip install langchain langchain-openai
   ```
3. Open the notebook:
   ```bash
   jupyter notebook Session2_Student_Prompt_Engineering.ipynb
   ```

### What's Inside

- **6 Demos** — Follow along with the instructor to see prompting techniques applied to McKinsey consulting scenarios.
- **8 Hands-On Tasks** — Complete the TODO sections to build your own agentic prompts for consulting use cases.

### Task Summary

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Design system prompts for a McKinsey Industry Research Agent | Beginner |
| Task 2 | Implement ReAct-style prompting for PE due diligence | Intermediate |
| Task 3 | Create a reusable McKinsey prompt template library | Intermediate |
| Task 4 | Build a McKinsey Analyst Agent with consulting tools | Advanced |
| Task 5 | Prompt chaining for M&A due diligence pipeline | Intermediate |
| Task 6 | Self-consistency voting for market sizing | Intermediate |
| Task 7 | Multi-persona debate for strategic decisions | Advanced |
| Task 8 | Guardrails & output validation for client deliverables | Advanced |

### Tips

- Pay close attention to how small prompt changes lead to very different outputs
- All scenarios use McKinsey consulting context — think about how you would frame prompts for real client work
- ReAct (Task 2) follows a Thought → Action → Observation loop — keep this pattern
- For Task 4, the agent decides which consulting tool to call at each step — this previews Day 2 tool-calling
