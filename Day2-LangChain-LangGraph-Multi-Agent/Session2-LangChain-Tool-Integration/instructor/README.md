# Session 2 — Instructor Notebook

## LangChain Development & Tool Integration

### Teaching Notes

**Duration:** 1 hour 45 minutes (11:00 – 12:45)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Introduction | 10 min | LangChain overview, why frameworks matter |
| Demo 1 | 10 min | ChatModels and PromptTemplates |
| Demo 2 | 12 min | LCEL chains with pipe operator |
| Demo 3 | 12 min | Custom tool creation |
| Demo 4 | 10 min | Document loading and splitting |
| Demo 5 | 10 min | Simple RAG pipeline |
| Task 1 | 10 min | Chain with output parsers |
| Task 2 | 10 min | Custom tools |
| Task 3 | 10 min | Conversational chain with memory |
| Task 4 | 15 min | RAG Q&A system |
| Wrap-up | 6 min | Q&A and key takeaways |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary and talking points
- **4 Solved Tasks** — Complete solutions with step-by-step explanations

### Key Teaching Points

1. LangChain provides composable building blocks — emphasize the Runnable interface as the unifying abstraction
2. LCEL is the modern way to build chains — discourage legacy LLMChain usage
3. Tools are what make agents useful — show how the `@tool` decorator simplifies creation
4. RAG is the most common production pattern — connect it to agentic retrieval in later sessions

### Common Student Questions

- "Why use LangChain instead of raw OpenAI calls?" — Composability, tool integration, memory, and ecosystem
- "What is LCEL vs. the old chain API?" — LCEL is the current standard; old chains are legacy
- "How does RAG differ from fine-tuning?" — RAG adds context at inference time; fine-tuning changes model weights
