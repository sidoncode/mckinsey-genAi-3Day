# Session 2: Prompt Engineering for Agentic Behaviors

**Time:** 11:00 – 12:45 (1 hour 45 minutes)

## Overview

This session dives deep into prompt engineering techniques specifically designed to drive agentic behaviors. Participants will learn how to craft system prompts, implement reasoning patterns like Chain-of-Thought and ReAct, generate structured outputs, manage multi-turn conversations, and use LangChain for reusable prompt workflows — all applied to **McKinsey consulting scenarios** including client feedback classification, retail restructuring analysis, and engagement planning.

## Key Topics

- Zero-shot vs. few-shot prompting for client feedback classification
- Chain-of-Thought (CoT) reasoning for structured consulting analysis
- Role-based prompting with McKinsey practice-area personas
- Structured output generation (JSON mode) for client data extraction
- Multi-turn conversation management for engagement planning
- LangChain prompt templates and structured output parsers

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session2_Student_Prompt_Engineering.ipynb` | 6 guided demos + 8 TODO exercises with hints |
| `instructor/Session2_Instructor_Prompt_Engineering.ipynb` | 6 fully solved demos + 8 exercises with explanations |

## Demos (6)

1. **Demo 1:** Zero-shot vs. few-shot prompting — McKinsey client engagement feedback classification
2. **Demo 2:** Chain-of-Thought prompting — retail restructuring revenue analysis
3. **Demo 3:** Role-based personas — Growth Strategy, Risk & Compliance, Organization & People leads
4. **Demo 4:** Structured output (JSON mode) — extracting client executive profiles from meeting notes
5. **Demo 5:** Multi-turn conversation — insurance engagement planning with context accumulation
6. **Demo 6:** LangChain prompt templates — structured consulting deliverables with output parsers

## Exercises (8)

1. **Task 1:** Design system prompts for a McKinsey Industry Research Agent
2. **Task 2:** Implement ReAct-style prompting for PE due diligence
3. **Task 3:** Create a reusable McKinsey prompt template library (market sizing, executive briefing, competitive analysis)
4. **Task 4:** Build a McKinsey Analyst Agent with consulting tools (market database, financial model, benchmarking)
5. **Task 5:** Prompt chaining for M&A due diligence pipeline (3-stage: extract metrics → strategic fit → recommendation)
6. **Task 6:** Self-consistency voting for market sizing (run N times, aggregate for robust estimate)
7. **Task 7:** Multi-persona debate for strategic decisions (Bull vs. Bear analysts + moderator synthesis)
8. **Task 8:** Guardrails & output validation for client deliverables (LLM-as-judge with auto-retry)
