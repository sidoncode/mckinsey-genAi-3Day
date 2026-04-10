# Track B — Student Notebook

## McKinsey Engagement Team (Multi-Agent Capstone)

### Setup Instructions

1. Ensure Python 3.9+ is installed
2. Install required packages:
   ```bash
   pip install openai langchain langchain-openai langgraph pydantic
   ```
3. Set your API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
4. Open the notebook:
   ```bash
   jupyter notebook Session3_Student_Track_B_Multi_Agent.ipynb
   ```

### What's Inside

- **Guided capstone project** — build a McKinsey Engagement Team simulation with 6 milestones
- Each milestone builds on the previous one
- TODO placeholders with detailed hints at each step

### Milestone Summary

| Milestone | Topic | Duration |
|---|---|---|
| Milestone 1 | EngagementManagerAgent supervisor & workstream decomposition | ~20 min |
| Milestone 2 | Specialist consulting agents (Strategy, Financial, Operations, Industry) | ~25 min |
| Milestone 3 | LangGraph engagement orchestration | ~25 min |
| Milestone 4 | Partner Review quality loop for deliverable refinement | ~25 min |
| Milestone 5 | Cross-agent memory and context sharing | ~15 min |
| Milestone 6 | Engagement analytics and reporting dashboard | ~15 min |

### Tips

- Work through milestones in order — each builds on the last
- Test each consulting agent individually before orchestrating them together
- Think about what a Partner Review looks for: strategic coherence, MECE structure, actionable recommendations
- You will present your McKinsey Engagement Team system in Session 4
