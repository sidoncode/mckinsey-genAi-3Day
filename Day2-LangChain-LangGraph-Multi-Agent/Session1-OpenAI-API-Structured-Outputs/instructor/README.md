# Session 1 — Instructor Notebook

## OpenAI API Engineering with Structured Outputs

### Teaching Notes

**Duration:** 1 hour 45 minutes (9:00 – 10:45)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 10 min | Session overview, connection to Day 1 consulting foundations |
| Demo 1 | 10 min | API deep dive — streaming CEO briefings, token tracking |
| Demo 2 | 12 min | JSON mode — client profile extraction |
| Demo 3 | 12 min | Function calling — market research tool |
| Demo 4 | 10 min | Pydantic EngagementSummary validation |
| Demo 5 | 10 min | Engagement team extraction pipeline |
| Task 1 | 10 min | Competitive intelligence extractor |
| Task 2 | 10 min | Financial analysis tool |
| Task 3 | 10 min | Multi-tool consulting agent |
| Task 4 | 15 min | RobustConsultingClient |
| Task 5 | 10 min | Parallel function calling |
| Task 6 | 12 min | Nested Pydantic deal memo |
| Task 7 | 12 min | Multi-turn tool agent with memory |
| Task 8 | 10 min | Batch processing pipeline |
| Wrap-up | 6 min | Q&A and key takeaways |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and McKinsey consulting talking points
- **8 Solved Tasks** — Complete solutions with step-by-step explanations

### Key Teaching Points

1. Structured outputs are essential for consulting AI systems — engagement data must be machine-readable for downstream workflows
2. Function calling enables LLMs to interact with consulting tools (market research, financial analysis, benchmarking)
3. Pydantic is the industry standard for validating LLM outputs — demonstrate with EngagementSummary and client profile models
4. Connect structured outputs to downstream consulting workflows (engagement pipelines, partner dashboards)

### Common Student Questions

- "When should I use JSON mode vs. function calling?" — JSON mode for simple structures (client profiles); function calling when the model should decide which consulting tool to use
- "Why Pydantic instead of plain dicts?" — Type safety, validation, auto-documentation — critical for consulting data quality
- "What happens when the model returns invalid JSON?" — Show retry logic and fallback strategies in the RobustConsultingClient
