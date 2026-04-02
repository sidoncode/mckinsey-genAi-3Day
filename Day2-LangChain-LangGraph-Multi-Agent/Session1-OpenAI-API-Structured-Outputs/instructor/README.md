# Session 1 — Instructor Notebook

## OpenAI API Engineering with Structured Outputs

### Teaching Notes

**Duration:** 1 hour 45 minutes (9:00 – 10:45)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 10 min | Session overview, connection to Day 1 |
| Demo 1 | 10 min | API deep dive — streaming, usage tracking |
| Demo 2 | 12 min | JSON mode structured outputs |
| Demo 3 | 12 min | Function calling / tool use |
| Demo 4 | 10 min | Pydantic validation of responses |
| Demo 5 | 10 min | Structured data extraction pipeline |
| Task 1 | 10 min | Entity extractor with JSON mode |
| Task 2 | 10 min | Calculator tool with function calling |
| Task 3 | 10 min | Multi-tool agent |
| Task 4 | 15 min | Robust API client |
| Wrap-up | 6 min | Q&A and key takeaways |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and talking points
- **4 Solved Tasks** — Complete solutions with step-by-step explanations

### Key Teaching Points

1. Emphasize that structured outputs are essential for agentic systems — agents must produce machine-readable data
2. Show how function calling enables LLMs to interact with external tools reliably
3. Highlight Pydantic as the industry standard for validating LLM outputs in Python
4. Connect structured outputs to downstream agentic workflows (tool use, planning, routing)

### Common Student Questions

- "When should I use JSON mode vs. function calling?" — JSON mode for simple structures; function calling when you want the model to decide which tool to use
- "Why Pydantic instead of plain dicts?" — Type safety, validation, auto-documentation, and IDE support
- "What happens when the model returns invalid JSON?" — Show retry logic and fallback strategies
