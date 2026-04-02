# Day 2 — LangChain, LangGraph & Multi-Agent Development

Welcome to Day 2 of the **Agentic AI Systems** training program. Building on Day 1's foundations, this day takes you from raw API engineering to production-grade agentic frameworks — structured outputs with the OpenAI API, LangChain for tool-augmented chains, LangGraph for stateful workflow orchestration, and multi-agent architectures for complex problem-solving.

---

## Schedule

| Time | Session | Focus |
|---|---|---|
| 9:00–10:45 | Session 1 | Module 4: OpenAI API Engineering with Structured Outputs |
| 10:45–11:00 | Break | |
| 11:00–12:45 | Session 2 | Module 5: LangChain Development & Tool Integration |
| 12:45–1:30 | Lunch | |
| 1:30–3:15 | Session 3 | Module 6: LangGraph Orchestration & Workflow Design |
| 3:15–3:30 | Break | |
| 3:30–5:00 | Session 4 | Module 7: Multi-Agent Workflows & Agentic Systems |

---

## Folder Structure

```
Day2-LangChain-LangGraph-Multi-Agent/
├── README.md
├── Session1-OpenAI-API-Structured-Outputs/
│   ├── README.md
│   ├── student/
│   │   ├── README.md
│   │   └── Session1_Student_OpenAI_API_Structured_Outputs.ipynb
│   └── instructor/
│       ├── README.md
│       └── Session1_Instructor_OpenAI_API_Structured_Outputs.ipynb
├── Session2-LangChain-Tool-Integration/
│   ├── README.md
│   ├── student/
│   │   ├── README.md
│   │   └── Session2_Student_LangChain_Tool_Integration.ipynb
│   └── instructor/
│       ├── README.md
│       └── Session2_Instructor_LangChain_Tool_Integration.ipynb
├── Session3-LangGraph-Orchestration/
│   ├── README.md
│   ├── student/
│   │   ├── README.md
│   │   └── Session3_Student_LangGraph_Orchestration.ipynb
│   └── instructor/
│       ├── README.md
│       └── Session3_Instructor_LangGraph_Orchestration.ipynb
└── Session4-Multi-Agent-Workflows/
    ├── README.md
    ├── student/
    │   ├── README.md
    │   └── Session4_Student_Multi_Agent_Workflows.ipynb
    └── instructor/
        ├── README.md
        └── Session4_Instructor_Multi_Agent_Workflows.ipynb
```

---

## How to Use

### For Students
- Open the **student/** notebook for the current session.
- Each notebook contains **5 guided demos** to follow along and **4 hands-on tasks** with TODO placeholders and hints.
- Complete each task by filling in the code where indicated.
- Refer to the student `README.md` for setup instructions and task summaries.

### For Instructors
- Open the **instructor/** notebook for the current session.
- Each notebook contains the **same 5 demos** with detailed commentary and **4 fully solved tasks** with explanations.
- Use these as a reference during live delivery or for review.
- Refer to the instructor `README.md` for teaching notes and timing guidance.

---

## Prerequisites

- Completion of **Day 1 — Foundations, Prompting & Evaluation**
- Python 3.9+
- Jupyter Notebook / JupyterLab
- An OpenAI API key (set as `OPENAI_API_KEY` environment variable)
- Required packages:

```bash
pip install openai tiktoken pydantic langchain langchain-openai langchain-community langgraph langsmith pandas matplotlib numpy
```

---

## Learning Outcomes

By the end of Day 2, participants will be able to:

1. Engineer structured, validated outputs from the OpenAI API using JSON mode, function calling, and Pydantic
2. Build tool-augmented LLM chains with LangChain and LCEL
3. Design stateful, branching workflows using LangGraph's StateGraph
4. Architect multi-agent systems with supervisor, worker, and handoff patterns
