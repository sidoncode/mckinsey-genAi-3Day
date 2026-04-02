# Session 2 — Instructor Notebook

## Deployment and Scaling

### Teaching Notes

**Duration:** 1 hour 45 minutes (11:00 – 12:45)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 10 min | Production vs. prototype mindset |
| Demo 1 | 10 min | FastAPI LLM service pattern |
| Demo 2 | 12 min | Caching and cost optimization |
| Demo 3 | 12 min | Monitoring and logging |
| Demo 4 | 10 min | Rate limiting and degradation |
| Demo 5 | 10 min | Model routing strategies |
| Task 1 | 10 min | Cached API endpoint |
| Task 2 | 10 min | Cost tracking system |
| Task 3 | 10 min | Monitoring dashboard |
| Task 4 | 12 min | Architecture design exercise |
| Track Selection | 9 min | Explain tracks, let students choose |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and talking points
- **4 Solved Tasks** — Complete solutions with step-by-step explanations

### Key Teaching Points

1. Caching is the #1 cost optimization — hash-based exact match and semantic similarity caching
2. Monitor the four golden signals: latency, throughput, errors, saturation
3. Model routing (cheap model for simple tasks, expensive for complex) can cut costs 60-80%
4. Design for failure: retries, circuit breakers, fallback responses

### Track Selection Guidance (end of session)

- **Track A (Production RAG Service):** Best for participants interested in data engineering, search, and information retrieval
- **Track B (Multi-Agent Orchestration):** Best for participants interested in agent architectures, workflows, and autonomous systems
- Both tracks are equally valuable — choose based on interest, not difficulty

### Common Student Questions

- "How much does it cost to run an LLM app?" — Walk through a cost calculation with token prices
- "Should I self-host or use an API?" — API for most use cases; self-host only for compliance/latency requirements
- "How do I handle spikes in traffic?" — Queue-based architecture with auto-scaling workers
