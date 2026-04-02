# Session 3 — Instructor Notebook

## LangGraph Orchestration & Workflow Design

### Teaching Notes

**Duration:** 1 hour 45 minutes (1:30 – 3:15)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 10 min | Why graphs? LangGraph vs. chains |
| Demo 1 | 10 min | StateGraph basics |
| Demo 2 | 12 min | Conditional edges and routing |
| Demo 3 | 12 min | ReAct agent pattern |
| Demo 4 | 10 min | Cycles and iterative refinement |
| Demo 5 | 10 min | Human-in-the-loop checkpointing |
| Task 1 | 10 min | Linear workflow |
| Task 2 | 10 min | Conditional routing |
| Task 3 | 10 min | Self-correcting code generation |
| Task 4 | 15 min | Research agent |
| Wrap-up | 6 min | Q&A and key takeaways |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and talking points
- **4 Solved Tasks** — Complete solutions with step-by-step explanations

### Key Teaching Points

1. LangGraph makes agent control flow explicit — contrast with implicit chain execution
2. State is the central concept — everything flows through the shared TypedDict
3. Conditional edges are what make agents intelligent — they route based on LLM decisions
4. Cycles enable self-correction and iterative refinement — a key agentic pattern

### Common Student Questions

- "How is LangGraph different from LangChain?" — LangChain is for linear chains; LangGraph adds branching, cycles, and state
- "Can I use LangGraph without LangChain?" — Yes, but they integrate well together
- "When should I use cycles vs. linear graphs?" — Cycles for self-correction, retries, or iterative improvement
