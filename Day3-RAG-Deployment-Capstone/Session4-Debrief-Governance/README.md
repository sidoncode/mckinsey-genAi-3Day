# Session 4: Cross-Track Debrief, Consulting AI Governance & Closing Reflection

**Time:** 3:30 – 5:00 (1 hour 30 minutes) | **Shared session — all participants**

## Overview

This closing session brings both capstone tracks together. Participants share what they built (McKinsey Knowledge Assistant or Engagement Team simulation), learn from each other's approaches, and then explore critical governance considerations for deploying AI in McKinsey consulting contexts — including client data protection, content quality guardrails, audit logging for engagement AI usage, and bias detection. The session closes with a structured reflection on the full 3-day program.

## Key Topics

- Cross-track capstone presentations and knowledge sharing
- AI governance frameworks for consulting AI systems
- Guardrails for client data protection and prompt injection prevention
- Content filtering for McKinsey quality standards
- Audit logging for engagement AI usage compliance
- Bias detection (industry and geographic bias in consulting recommendations)
- Deployment readiness assessment for consulting AI

## Notebooks

| Notebook | Description |
|---|---|
| `student/Session4_Student_Debrief_Governance.ipynb` | Guided discussions + governance exercises |
| `instructor/Session4_Instructor_Debrief_Governance.ipynb` | Facilitation guide with full solutions |

## Demos (5)

1. **Demo 1:** GuardrailSystem — blocked patterns and LLM safety classification for client data protection
2. **Demo 2:** ContentFilter — length, relevance, and quality checks for McKinsey standards
3. **Demo 3:** AuditLogger — tracking engagement AI usage for compliance
4. **Demo 4:** GovernanceEvaluator — 8-item McKinsey governance checklist (G1–G8)
5. **Demo 5:** GovernedAgent — combining guardrails, filtering, and logging into a governed consulting agent

## Exercises (6)

1. **Task 1:** Implement a PolicyGuardrail with configurable severity (block / warn / allow)
2. **Task 2:** Build a BiasDetector for industry and geographic bias in consulting recommendations
3. **Task 3:** Create a GovernanceScorecard with 8 McKinsey governance criteria
4. **Task 4:** Write a DeploymentReadiness assessment (technical / governance / operational)
5. **Task 5:** PII Detection and Redaction Pipeline — regex + LLM-based PII detection with auto-redaction
6. **Task 6:** Incident Response and Escalation System — severity classification, escalation rules, incident reporting
