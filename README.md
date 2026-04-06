# McKinsey GenAI 3-Day Workshop — Agentic AI Systems

A comprehensive **3-day, instructor-led training program** for building production-grade Agentic AI systems, designed for McKinsey consultants and enterprise engineering teams. Every demo, exercise, and scenario uses **McKinsey consulting context** — strategy engagements, M&A due diligence, digital transformation, market sizing, and client deliverables — so participants learn AI engineering through the lens of real consulting work.

The curriculum takes participants from LLM fundamentals through LangChain/LangGraph frameworks to production RAG pipelines and multi-agent orchestration — with hands-on coding in every session.

---

## What This Repo Contains

| Day | Theme | Sessions | Notebooks |
|-----|-------|----------|-----------|
| **Day 1** | Foundations, Prompting & Evaluation | 4 sessions (Modules 1-3 + Lab Review) | 5 notebooks |
| **Day 2** | LangChain, LangGraph & Multi-Agent | 4 sessions (Modules 4-7) | 8 notebooks |
| **Day 3** | RAG, Deployment, Capstone & Governance | 4 sessions (Modules 9-11) + 2 capstone tracks | 10 notebooks |

**Total: 23 Jupyter notebooks** (12 student + 11 instructor), **43 README files**, across **12 sessions** over 3 days.

Every session provides:
- **Student notebook** — Fully coded demos to follow along + hands-on tasks with TODO placeholders and hints
- **Instructor notebook** — Same demos + fully solved tasks with approach explanations and teaching notes
- **READMEs** at every level — session overview, student setup guide, instructor facilitation guide

All examples use **McKinsey consulting scenarios**: client engagement planning, MECE problem decomposition, Porter's Five Forces analysis, PE due diligence, post-merger integration, and market entry strategy.

---

## Program Schedule

### Day 1 — Foundations, Prompting & Evaluation

| Time | Session | Topic |
|------|---------|-------|
| 9:00 – 10:45 | Session 1 | **Module 1:** Modern LLM Foundations — architecture, tokenization, API parameters, embeddings, reasoning |
| 11:00 – 12:45 | Session 2 | **Module 2:** Prompt Engineering — few-shot, chain-of-thought, ReAct, LangChain templates |
| 1:30 – 3:15 | Session 3 | **Module 3:** Model Evaluation — metrics, LLM-as-Judge, benchmarking, sklearn metrics, DeepEval |
| 3:30 – 5:00 | Session 4 | **Lab Review & Integration** — facilitated review combining all Day 1 concepts |

### Day 2 — LangChain, LangGraph & Multi-Agent Development

| Time | Session | Topic |
|------|---------|-------|
| 9:00 – 10:45 | Session 1 | **Module 4:** OpenAI Structured Outputs — JSON mode, function calling, Pydantic |
| 11:00 – 12:45 | Session 2 | **Module 5:** LangChain — LCEL chains, custom tools, RAG pipelines |
| 1:30 – 3:15 | Session 3 | **Module 6:** LangGraph — StateGraph, conditional edges, cycles, ReAct agent |
| 3:30 – 5:00 | Session 4 | **Module 7:** Multi-Agent — supervisor-worker, handoffs, parallel execution |

### Day 3 — RAG, Deployment, Capstone & Debrief

| Time | Session | Topic |
|------|---------|-------|
| 9:00 – 10:45 | Session 1 | **Module 9:** RAG Deep Dive — embeddings, ChromaDB, chunking, query transformation |
| 11:00 – 12:45 | Session 2 | **Module 10:** Deployment & Scaling — API design, caching, monitoring, cost tracking |
| 1:30 – 3:15 | Session 3 | **Parallel Capstone Labs** — Track A: Production RAG Service / Track B: Multi-Agent Orchestration |
| 3:30 – 5:00 | Session 4 | **Module 11:** Cross-Track Debrief, Governance & Closing Reflection |

---

---

## Getting Started

### Prerequisites

- **Python 3.9+** (3.10 or 3.11 recommended)
- **Jupyter Notebook** or **JupyterLab**
- **OpenAI API key** with access to `gpt-4o-mini`, `gpt-4o`, and `text-embedding-3-small`

### 1. Clone the repository

```bash
git clone https://github.com/sidoncode/mckinsey-genAi-3Day.git
cd mckinsey-genAi-3Day
```

### 2. Create and activate a virtual environment

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

Install all packages needed across all 3 days in one command:

```bash
pip install openai tiktoken pydantic langchain langchain-openai langchain-community langgraph langsmith chromadb faiss-cpu pandas matplotlib numpy scikit-learn deepeval
```

Or install per day:

```bash
# Day 1 only
pip install openai tiktoken pandas matplotlib numpy scikit-learn deepeval langchain langchain-openai

# Day 2 (adds LangChain + LangGraph)
pip install openai tiktoken pydantic langchain langchain-openai langchain-community langgraph langsmith pandas matplotlib numpy

# Day 3 (adds vector stores)
pip install openai tiktoken pydantic langchain langchain-openai langchain-community langgraph chromadb faiss-cpu pandas matplotlib numpy
```

### 4. Set your OpenAI API key

**macOS / Linux:**

```bash
export OPENAI_API_KEY="sk-your-key-here"
```

**Windows (PowerShell):**

```powershell
$env:OPENAI_API_KEY="sk-your-key-here"
```

Or create a `.env` file at the repo root:

```
OPENAI_API_KEY=sk-your-key-here
```

### 5. Launch Jupyter and start a session

```bash
jupyter notebook
```

Navigate to the appropriate Day and Session folder, then open the **student/** or **instructor/** notebook.

---

## How to Use This Repo

### If you are a Student

1. **Follow the schedule** — open the student notebook for the current session.
2. **Run the demos** — each notebook starts with fully coded demos. Run each cell and read the commentary to understand the concepts.
3. **Complete the tasks** — after the demos, you will find hands-on tasks with `# YOUR CODE HERE` and `# TODO` placeholders. Each task includes hints to guide your implementation.
4. **McKinsey context** — all examples use consulting scenarios (M&A, market sizing, client engagements). Think about how each technique applies to real consulting work.
5. **Progress through days** — Day 1 builds foundations, Day 2 introduces frameworks, Day 3 puts it all together in a capstone project.
6. **On Day 3, choose your track** — at the end of Session 2, select Track A (Production RAG Service) or Track B (Multi-Agent Orchestration) for the capstone lab.

### If you are an Instructor

1. **Use the instructor notebooks** — they contain the same demos plus fully solved versions of all tasks with detailed approach explanations.
2. **Check each session's instructor README** — it includes a timing table, key teaching points, common student questions, and facilitation tips.
3. **Leverage the McKinsey context** — all scenarios are designed around consulting work. Encourage participants to think about how they would apply each technique in real engagements.
4. **For Day 3 Session 3** — split the room into two tracks. Each track has a self-contained capstone with progressive milestones.
5. **For Day 3 Session 4** — facilitate cross-track presentations (2 min each), then work through governance demos and exercises.

### If you are Self-Studying

1. Start with the **student notebooks** and attempt each task yourself.
2. When stuck, check the **instructor notebook** for the same session to see the solution and approach explanation.
3. Work through all 3 days in order — the material is cumulative.
4. For the Day 3 capstone, try **both** tracks for maximum learning.

---

## Technical Stack

### Core LLM Platform

| Technology | Purpose | Used In |
|-----------|---------|---------|
| **OpenAI API** | LLM inference (chat completions, embeddings) | All 3 days |
| **GPT-4o-mini** | Primary model for demos and tasks (fast, cost-effective) | All 3 days |
| **GPT-4o** | Complex tasks, model routing for advanced queries | Day 2-3 |
| **text-embedding-3-small** | Text embedding for semantic search and RAG | Day 1, Day 3 |

### Frameworks & Libraries

| Technology | Purpose | Used In |
|-----------|---------|---------|
| **LangChain** | LLM application framework — chains, prompts, tools, output parsers | Day 1-3 |
| **LangChain LCEL** | Declarative chain composition using the pipe (`|`) operator | Day 2-3 |
| **LangGraph** | Stateful graph-based workflow orchestration with cycles and conditional edges | Day 2-3 |
| **ChromaDB** | In-memory vector database for embedding storage and similarity search | Day 3 |
| **FAISS** | High-performance vector similarity search (alternative to ChromaDB) | Day 3 |
| **DeepEval** | LLM evaluation framework with G-Eval and relevancy metrics | Day 1 |

### Data & Validation

| Technology | Purpose | Used In |
|-----------|---------|---------|
| **Pydantic** | Data validation, structured output schemas | Day 2-3 |
| **tiktoken** | OpenAI tokenizer for token counting and cost estimation | Day 1-2 |
| **scikit-learn** | Classification metrics (precision, recall, F1) for evaluation | Day 1 |
| **NumPy** | Numerical operations (cosine similarity, metrics) | Day 1-3 |
| **Pandas** | Data analysis and tabular output | Day 1 |
| **Matplotlib** | Visualization of evaluation metrics and embeddings | Day 1 |

### Key Patterns Covered

| Pattern | Description | Session |
|---------|-------------|---------|
| **Prompt Engineering** | Few-shot, chain-of-thought, ReAct — applied to McKinsey consulting analysis | Day 1, Session 2 |
| **Embeddings & Vectors** | Consulting document embeddings, similarity, PCA/t-SNE visualization | Day 1, Session 1 |
| **LLM Reasoning** | MECE decomposition, engagement planning, tool selection for consulting workflows | Day 1, Session 1 |
| **Structured Outputs** | JSON mode, function calling, Pydantic — extracting client profiles and engagement data | Day 1-2 |
| **LCEL Chains** | Composable prompt → model → parser pipelines for consulting analysis | Day 2, Session 2 |
| **Tool Use** | Custom consulting tools (market research, financial modeling, benchmarking) | Day 2, Session 2 |
| **StateGraph Workflows** | Conditional edges, cycles — modeling consulting engagement lifecycles | Day 2, Session 3 |
| **Multi-Agent Systems** | Supervisor-worker teams modeling McKinsey engagement structures | Day 2, Session 4 |
| **RAG Pipeline** | Embed → index → retrieve → generate with McKinsey knowledge bases | Day 3, Session 1 |
| **Advanced Chunking** | Recursive, markdown-aware splitting of consulting reports and whitepapers | Day 3, Session 1 |
| **Query Transformation** | Multi-query expansion, HyDE for comprehensive consulting research | Day 3, Session 1 |
| **Semantic Caching** | Embedding-based cache for similar consulting queries | Day 3, Session 2 |
| **Model Routing** | Complexity-based routing (simple lookups vs. strategy analysis) | Day 3, Session 2 |
| **LLM-as-Judge Evaluation** | Automated quality scoring for consulting deliverables | Day 1, Day 3 |
| **AI Governance** | Guardrails, bias detection, audit logging for consulting AI deployment | Day 3, Session 4 |

---

## McKinsey Consulting Context

All exercises throughout the program use realistic McKinsey consulting scenarios:

- **Strategy & Growth:** Market entry assessments, Three Horizons of Growth analysis, competitive landscape mapping
- **M&A & Due Diligence:** Post-merger integration, PE portfolio company evaluation, deal screening
- **Digital Transformation:** Omnichannel retail strategy, AI-powered diagnostics, supply chain digitization
- **Operations Excellence:** Cost optimization programs, supply chain resilience, operating model design
- **Client Engagement:** CEO briefings, engagement scoping, MECE problem decomposition, deliverable preparation
- **Frameworks:** Porter's Five Forces, 7-S Model, Value Chain Analysis, Growth-Share Matrix

---

## Learning Outcomes

By completing this program, participants will be able to:

**Day 1 — Foundations**
1. Explain modern LLM architectures, embeddings, and reasoning capabilities for agentic consulting systems
2. Apply prompt engineering techniques (few-shot, CoT, ReAct) to McKinsey consulting analysis and deliverables
3. Evaluate and compare LLM models using structured metrics, sklearn classification metrics, and DeepEval

**Day 2 — Frameworks**
4. Engineer structured outputs using JSON mode, function calling, and Pydantic for consulting data extraction
5. Build tool-augmented LLM chains with LangChain and LCEL for consulting analysis pipelines
6. Design stateful consulting workflows with LangGraph (StateGraph, conditional edges, cycles)
7. Architect multi-agent systems modeling McKinsey engagement teams with supervisor-worker patterns

**Day 3 — Production**
8. Build production RAG pipelines with McKinsey knowledge bases, embeddings, vector stores, and reranking
9. Deploy consulting AI services with caching, monitoring, model routing, and cost controls
10. Complete an end-to-end capstone project (Production RAG or Multi-Agent system) for consulting use cases
11. Evaluate AI systems against governance criteria and design deployment readiness assessments for consulting firms

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'openai'` | Run `pip install openai` inside your activated virtual environment |
| `AuthenticationError` from OpenAI | Verify `OPENAI_API_KEY` is set: `echo $OPENAI_API_KEY` (macOS/Linux) or `echo %OPENAI_API_KEY%` (Windows) |
| `RateLimitError` from OpenAI | You have hit your API rate limit. Wait 60 seconds and retry, or check your OpenAI usage dashboard |
| ChromaDB import errors | Run `pip install chromadb` — requires Python 3.9+ |
| LangGraph import errors | Run `pip install langgraph` — requires `langchain-core >= 0.2` |
| DeepEval import errors | Run `pip install deepeval` — requires Python 3.9+ |
| Notebooks not rendering | Ensure Jupyter is installed: `pip install jupyter` and launch with `jupyter notebook` |
| FAISS install fails on Apple Silicon | Use `pip install faiss-cpu` (not `faiss-gpu`) |

---

## License

This repository is for educational purposes as part of the McKinsey GenAI training program.
