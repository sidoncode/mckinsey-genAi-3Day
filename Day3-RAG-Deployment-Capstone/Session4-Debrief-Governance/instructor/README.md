# Session 4 — Instructor Notebook

## Cross-Track Debrief, Consulting AI Governance & Closing

### Teaching Notes

**Duration:** 1 hour 30 minutes (3:30 – 5:00)

### Suggested Timing

| Segment | Duration | Content |
|---|---|---|
| Cross-Track Presentations | 20 min | 2-3 demos per track (Knowledge Assistant / Engagement Team), Q&A |
| Demo 1 | 8 min | GuardrailSystem — client data protection |
| Demo 2 | 8 min | ContentFilter — McKinsey quality standards |
| Demo 3 | 8 min | AuditLogger — engagement AI compliance |
| Demo 4 | 8 min | GovernanceEvaluator — McKinsey checklist (G1–G8) |
| Demo 5 | 5 min | GovernedAgent — full governance stack |
| Task 1-2 | 12 min | PolicyGuardrail & BiasDetector |
| Task 3-4 | 12 min | GovernanceScorecard & DeploymentReadiness |
| Task 5 | 10 min | PII Detection and Redaction Pipeline |
| Task 6 | 10 min | Incident Response and Escalation System |
| Closing Reflection | 9 min | Retrospective, resources, next steps |

### What's Inside

- **5 Demos** — Fully executed with detailed commentary on McKinsey consulting AI governance
- **6 Solved Tasks** — Complete solutions with explanations
- **Facilitation guide** for cross-track capstone presentations

### Key Teaching Points

1. Governance is an engineering discipline for consulting AI, not a checkbox — build it into the system from day one
2. Client data protection is non-negotiable — guardrails must prevent leakage of confidential engagement data
3. Every consulting AI system needs an audit trail — who used what AI capability, for which engagement, and what was generated
4. Bias detection matters for consulting: industry bias (always recommending tech solutions) and geographic bias (assuming US market norms)

### Facilitation Tips for Cross-Track Presentations

- Ask each track for 2-3 volunteer presenters (2 min each)
- Track A presents their McKinsey Knowledge Assistant (RAG pipeline, retrieval quality, MECE answers)
- Track B presents their McKinsey Engagement Team (agent collaboration, Partner Review loop, deliverable quality)
- Highlight how production systems often combine both approaches — Knowledge Assistants feeding data to Engagement Teams

### Common Student Questions

- "How do I prevent my consulting agent from leaking client data?" — Guardrails with blocked patterns, input/output filtering, and audit logging
- "Is there a standard governance framework?" — NIST AI RMF, EU AI Act, and McKinsey's internal AI governance policies
- "What should I learn next?" — Suggest advanced RAG patterns, production agent deployment, and McKinsey-specific AI tools
