# Session 2: Deployment and Scaling

**Time:** 11:00 – 12:45 (1 hour 45 minutes) | **Shared session — all participants**

## Overview

This session bridges the gap between notebook prototypes and production systems. Participants will learn the architecture patterns, cost optimization techniques, monitoring strategies, and scaling considerations needed to deploy LLM-powered applications in the real world. Track selection for the afternoon capstone happens at the close of this session.

## Key Topics

- LLM application architecture patterns (API services, async workers, streaming)
- Cost optimization: caching, model routing, prompt compression
- Monitoring and observability for LLM applications
- Rate limiting, retry strategies, and graceful degradation
- Scaling considerations: horizontal scaling, load balancing, queue-based architectures

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session2_Student_Deployment_Scaling.ipynb` | Guided demos + TODO exercises with hints |
| `instructor/Session2_Instructor_Deployment_Scaling.ipynb` | Fully solved demos + exercises with explanations |

## Demos (5)

1. **Demo 1:** Building an LLM API service with FastAPI
2. **Demo 2:** Response caching and cost optimization
3. **Demo 3:** Monitoring and logging LLM calls
4. **Demo 4:** Rate limiting and graceful degradation
5. **Demo 5:** Model routing — choosing the right model per request

## Exercises (4)

1. **Task 1:** Build a cached LLM API endpoint
2. **Task 2:** Implement a cost tracking and budget system
3. **Task 3:** Create a monitoring dashboard for LLM metrics
4. **Task 4:** Design a production deployment architecture (diagramming exercise)
