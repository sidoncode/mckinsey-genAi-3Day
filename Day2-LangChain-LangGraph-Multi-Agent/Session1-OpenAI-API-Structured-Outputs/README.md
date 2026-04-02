# Session 1: OpenAI API Engineering with Structured Outputs

**Time:** 9:00 – 10:45 (1 hour 45 minutes)

## Overview

This session moves beyond basic chat completions into production-grade API engineering. Participants will master structured output generation using JSON mode, function calling (tool use), and Pydantic validation — skills essential for building reliable agentic systems that produce machine-readable outputs.

## Key Topics

- OpenAI Chat Completions API deep dive (streaming, usage tracking)
- Structured outputs with JSON mode and `response_format`
- Function calling / tool use with the OpenAI API
- Pydantic models for response parsing and validation
- Building robust API wrappers with retries and error handling

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session1_Student_OpenAI_API_Structured_Outputs.ipynb` | Guided demos + TODO exercises with hints |
| `instructor/Session1_Instructor_OpenAI_API_Structured_Outputs.ipynb` | Fully solved demos + exercises with explanations |

## Demos (5)

1. **Demo 1:** OpenAI API deep dive — streaming, token usage, and finish reasons
2. **Demo 2:** Structured output with JSON mode
3. **Demo 3:** Function calling — defining and using tools
4. **Demo 4:** Pydantic-based response validation
5. **Demo 5:** Building a structured data extraction pipeline

## Exercises (4)

1. **Task 1:** Build a structured entity extractor using JSON mode
2. **Task 2:** Implement a calculator tool with function calling
3. **Task 3:** Create a multi-tool agent with automatic tool dispatch
4. **Task 4:** Build a robust API client with retries, validation, and streaming
