# Session 1: Modern LLM Foundations for Agentic Systems

**Time:** 9:00 – 10:45 (1 hour 45 minutes)

## Overview

This session introduces the foundational concepts of Large Language Models (LLMs) that underpin agentic AI systems. Participants will learn how LLMs work under the hood, explore tokenization, context windows, model parameters, embeddings, and reasoning capabilities — all applied to **McKinsey consulting scenarios** including digital transformation strategy, market analysis, and engagement planning.

## Key Topics

- LLM architecture overview (Transformer, attention mechanisms)
- Tokenization and context window management with consulting text
- Model parameters: temperature, top_p, frequency_penalty, max_tokens
- API setup and configuration (OpenAI) with environment variables
- Building LLM pipelines for consulting use cases
- Embeddings and vector representations for semantic search
- API cost estimation and engagement budgeting
- Context-aware routing agents with practice-specific personas

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session1_Student_LLM_Foundations.ipynb` | 5 guided demos + 8 TODO exercises with hints |
| `instructor/Session1_Instructor_LLM_Foundations.ipynb` | 5 demos + 8 exercises with full solutions and approach explanations |

## Demos (5)

1. **Demo 1:** Setting up LLM API connections — McKinsey digital transformation query
2. **Demo 2:** Understanding tokenization — consulting terminology and context window analysis
3. **Demo 3:** Exploring model parameters — temperature, top_p, max_tokens comparison
4. **Demo 4:** Role-based personas — McKinsey Partner, Associate, and Expert analyzing retail decline
5. **Demo 5:** Building a basic LLM pipeline — research summarization for client decks

## Exercises (8)

| Task | Topic | Difficulty |
|---|---|---|
| Task 1 | Test API connection with McKinsey MECE problem-solving prompt | Beginner |
| Task 2 | Optimize token usage on a healthcare market research brief | Intermediate |
| Task 3 | Compare temperature settings on competitive advantage analysis | Intermediate |
| Task 4 | Build a SimpleAgent as a McKinsey engagement manager | Intermediate |
| Task 5 | Generate and compare embeddings for semantic search | Intermediate |
| Task 6 | Build a multi-step analysis pipeline with quality review | Advanced |
| Task 7 | Estimate API costs from token usage for engagement budgeting | Intermediate |
| Task 8 | Build a context-aware routing agent with practice-specific personas | Advanced |

## Environment Variables

All notebooks load configuration from the project root `.env` file via `python-dotenv`. Key variables used in this session:

| Variable | Default | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | *(required)* | OpenAI API authentication |
| `OPENAI_MODEL_NAME` | `gpt-4o-mini` | Chat model used across demos and tasks |
| `OPENAI_EMBEDDING_MODEL` | `text-embedding-3-small` | Embedding model for Task 5 |
| `DEFAULT_TEMPERATURE` | `0` | Default LLM temperature |
| `DEFAULT_MAX_TOKENS` | `300` | Default max response tokens |
