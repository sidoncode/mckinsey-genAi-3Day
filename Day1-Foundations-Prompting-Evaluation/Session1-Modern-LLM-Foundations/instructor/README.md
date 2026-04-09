# Session 1 — Instructor Notebook

## Modern LLM Foundations for Agentic Systems

### Teaching Notes

**Duration:** 1 hour 45 minutes (9:00 – 10:45)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 8 min | Session overview, learning objectives |
| Demo 1 | 8 min | API connections — McKinsey digital transformation query |
| Demo 2 | 10 min | Tokenization — consulting terminology analysis |
| Demo 3 | 8 min | Model parameters — executive summary generation |
| Demo 4 | 8 min | Role-based personas — Partner, Associate, Expert on retail |
| Demo 5 | 8 min | LLM pipeline — research summarization for client decks |
| Task 1 | 4 min | Test connection with MECE prompt |
| Task 2 | 6 min | Token optimization on healthcare brief |
| Task 3 | 5 min | Temperature comparison on competitive analysis |
| Task 4 | 8 min | Build McKinsey engagement manager agent |
| Task 5 | 8 min | Embeddings and cosine similarity for semantic search |
| Task 6 | 8 min | Multi-step analysis pipeline with quality review |
| Task 7 | 5 min | API cost estimation and engagement budgeting |
| Task 8 | 8 min | Context-aware routing agent with practice personas |
| Wrap-up | 5 min | Q&A and key takeaways |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and talking points
- **8 Solved Tasks** — Complete solutions with step-by-step explanations and approach descriptions

### Key Teaching Points

1. Emphasize that understanding tokens is critical for cost and context management in agents
2. Show how temperature affects creativity vs. determinism — agents need low temperature for reliability
3. Embeddings are the foundation of RAG systems — connect Task 5 to Day 3 RAG content
4. The multi-step pipeline (Task 6) introduces the self-reflection pattern — a key agentic capability
5. Cost estimation (Task 7) is a practical skill for scoping AI-augmented consulting engagements
6. The routing agent (Task 8) previews the classify-then-route pattern used in Day 2 multi-agent systems
7. All notebooks use `python-dotenv` to load environment variables — model names, temperatures, and max tokens are configurable without code changes

### Common Student Questions

- "Why not always use the largest context window?" — Cost, latency, and attention degradation
- "What temperature should agents use?" — Typically 0–0.3 for tool-calling; higher for creative tasks
- "How do embeddings relate to RAG?" — Embeddings enable semantic search over consulting knowledge bases
- "How expensive is it to run these queries?" — Task 7 covers this; gpt-4o-mini is very cost-effective for most consulting use cases
- "Why route to different personas instead of one system message?" — Specialization improves quality; this is the foundation for multi-agent architectures in Day 2
