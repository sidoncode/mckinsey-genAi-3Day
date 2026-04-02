# Day 1 — Foundations, Prompting & Evaluation

Welcome to Day 1 of the **Agentic AI Systems** training program. This day establishes the core building blocks — LLM fundamentals, prompt engineering for agentic behaviors, model evaluation, and integration of all three into a cohesive agentic system design.

---

## Schedule

| Time | Session | Focus |
|---|---|---|
| 9:00–10:45 | Session 1 | Module 1: Modern LLM Foundations for Agentic Systems |
| 10:45–11:00 | Break | |
| 11:00–12:45 | Session 2 | Module 2: Prompt Engineering for Agentic Behaviors |
| 12:45–1:30 | Lunch | |
| 1:30–3:15 | Session 3 | Module 3: Model Evaluation and Comparison |
| 3:15–3:30 | Break | |
| 3:30–5:00 | Session 4 | Day 1 Lab Review & Integration |

---

## Folder Structure

```
Day1-Foundations-Prompting-Evaluation/
├── README.md
├── Session1-Modern-LLM-Foundations/
│   ├── README.md
│   ├── student/
│   │   ├── README.md
│   │   └── Session1_Student_LLM_Foundations.ipynb
│   └── instructor/
│       ├── README.md
│       └── Session1_Instructor_LLM_Foundations.ipynb
├── Session2-Prompt-Engineering/
│   ├── README.md
│   ├── student/
│   │   ├── README.md
│   │   └── Session2_Student_Prompt_Engineering.ipynb
│   └── instructor/
│       ├── README.md
│       └── Session2_Instructor_Prompt_Engineering.ipynb
├── Session3-Model-Evaluation/
│   ├── README.md
│   ├── student/
│   │   ├── README.md
│   │   └── Session3_Student_Model_Evaluation.ipynb
│   └── instructor/
│       ├── README.md
│       └── Session3_Instructor_Model_Evaluation.ipynb
└── Session4-Lab-Review-Integration/
    ├── README.md
    ├── student/
    │   ├── README.md
    │   └── Session4_Student_Lab_Review.ipynb
    └── instructor/
        ├── README.md
        └── Session4_Instructor_Lab_Review.ipynb
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

- Python 3.9+
- Jupyter Notebook / JupyterLab
- An OpenAI API key (set as `OPENAI_API_KEY` environment variable)
- Required packages: `openai`, `tiktoken`, `pandas`, `matplotlib`, `numpy`

```bash
pip install openai tiktoken pandas matplotlib numpy
```

---

## Learning Outcomes

By the end of Day 1, participants will be able to:

1. Explain modern LLM architectures and their relevance to agentic systems
2. Apply prompt engineering techniques to drive agentic behaviors
3. Evaluate and compare LLM models using structured metrics
4. Integrate foundations, prompting, and evaluation into an agentic system prototype
