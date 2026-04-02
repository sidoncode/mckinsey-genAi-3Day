# Session 4 — Instructor Notebook

## Multi-Agent Workflows & Agentic Systems

### Teaching Notes

**Duration:** 1 hour 30 minutes (3:30 – 5:00)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 8 min | Multi-agent motivation and patterns overview |
| Demo 1 | 10 min | Supervisor-worker pattern |
| Demo 2 | 10 min | Agent handoff and communication |
| Demo 3 | 10 min | Parallel agent execution |
| Demo 4 | 10 min | Collaborative writing agents |
| Demo 5 | 10 min | End-to-end multi-agent system |
| Task 1 | 8 min | Two-agent supervisor-worker |
| Task 2 | 8 min | Agent handoff |
| Task 3 | 10 min | Parallel research pipeline |
| Task 4 | 12 min | Complete architecture design |
| Wrap-up | 4 min | Day 2 review and Day 3 preview |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and talking points
- **4 Solved Tasks** — Complete solutions with step-by-step explanations

### Key Teaching Points

1. Multi-agent systems decompose complex problems into specialized sub-tasks
2. The supervisor pattern is the most common starting point — one orchestrator, many workers
3. Agent handoff requires careful context management — what state transfers between agents
4. Not everything needs multi-agent — use the simplest architecture that solves the problem

### Common Student Questions

- "When should I use multi-agent vs. a single agent?" — When tasks require distinct expertise or can be parallelized
- "How do agents share information?" — Through shared state in LangGraph, or message passing
- "What about error handling across agents?" — Supervisor should handle failures and reassign or retry
