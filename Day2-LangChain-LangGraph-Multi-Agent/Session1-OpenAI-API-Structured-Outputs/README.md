# Session 1: OpenAI API Engineering with Structured Outputs

**Time:** 9:00 – 10:45 (1 hour 45 minutes)

## Overview

This session moves beyond basic chat completions into production-grade API engineering for McKinsey consulting applications. Participants will master structured output generation using JSON mode, function calling (tool use), and Pydantic validation — skills essential for building reliable consulting AI systems that produce machine-readable outputs from client engagements, market research, and financial analysis.

## Key Topics

- OpenAI Chat Completions API deep dive (streaming CEO briefings, token usage tracking)
- Structured outputs with JSON mode for client profile extraction
- Function calling / tool use for consulting tools (market research, financial analysis)
- Pydantic models for validating consulting data (EngagementSummary, client profiles)
- Building robust consulting API wrappers with retries and error handling

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session1_Student_OpenAI_API_Structured_Outputs.ipynb` | 5 guided demos + 8 TODO exercises with hints |
| `instructor/Session1_Instructor_OpenAI_API_Structured_Outputs.ipynb` | 5 fully solved demos + 8 exercises with explanations |

## Demos (5)

1. **Demo 1:** OpenAI API deep dive — streaming CEO briefings, token usage tracking
2. **Demo 2:** Structured output with JSON mode — extracting client profiles
3. **Demo 3:** Function calling — defining and using a market research tool
4. **Demo 4:** Pydantic-based EngagementSummary validation
5. **Demo 5:** Building an engagement team extraction pipeline

## Exercises (8)

1. **Task 1:** Build a competitive intelligence extractor from M&A briefings
2. **Task 2:** Implement a financial analysis tool with function calling (Meridian Health, Apex Energy)
3. **Task 3:** Create a multi-tool consulting agent (market_research + financial_analysis + benchmarking)
4. **Task 4:** Build a RobustConsultingClient with retries, Pydantic validation, and streaming
5. **Task 5:** Parallel function calling for cross-practice research (handle 2+ tool calls in one turn)
6. **Task 6:** Nested Pydantic models for M&A deal memo generation (TargetProfile + FinancialSummary + RiskAssessment)
7. **Task 7:** Multi-turn tool agent with conversation memory (stateful across follow-up questions)
8. **Task 8:** Batch processing pipeline with structured validation (process N engagement notes with error tracking)
