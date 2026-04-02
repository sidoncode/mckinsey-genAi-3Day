# Session 3: LangGraph Orchestration & Workflow Design

**Time:** 1:30 – 3:15 (1 hour 45 minutes)

## Overview

This session introduces LangGraph, a framework for building stateful, multi-step agentic workflows as directed graphs. Participants will learn to model complex agent behaviors using nodes, edges, and shared state — enabling conditional routing, iterative refinement loops, and human-in-the-loop patterns that go far beyond simple chains.

## Key Topics

- LangGraph fundamentals: StateGraph, nodes, and edges
- TypedDict state schemas and message passing
- Conditional edges for dynamic routing
- Cycles and iterative workflows
- Human-in-the-loop checkpointing

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session3_Student_LangGraph_Orchestration.ipynb` | Guided demos + TODO exercises with hints |
| `instructor/Session3_Instructor_LangGraph_Orchestration.ipynb` | Fully solved demos + exercises with explanations |

## Demos (5)

1. **Demo 1:** LangGraph basics — creating a simple StateGraph
2. **Demo 2:** Adding conditional edges for routing
3. **Demo 3:** Building a ReAct agent with LangGraph
4. **Demo 4:** Implementing cycles for iterative refinement
5. **Demo 5:** Human-in-the-loop with checkpointing

## Exercises (4)

1. **Task 1:** Build a simple linear workflow with LangGraph
2. **Task 2:** Create a conditional routing agent
3. **Task 3:** Implement a self-correcting code generation workflow
4. **Task 4:** Build a research agent with planning and execution nodes
