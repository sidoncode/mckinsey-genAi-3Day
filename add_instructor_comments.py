"""
Add instructor commentary (approach, common mistakes, skippability)
to all task/milestone markdown cells across all 11 instructor notebooks.
"""

import json
import os
import re

BASE = "/Users/siddharthsharma/Desktop/mckinsey-genAi-3Day"

# ============================================================
# INSTRUCTOR COMMENTARY FOR EVERY TASK/MILESTONE
# ============================================================
# Key: (notebook_path_suffix, task_identifier_substring)
# Value: dict with conducting, mistakes, skippable

COMMENTS = {
    # =========== DAY 1 SESSION 1 ===========
    ("Day1-Foundations-Prompting-Evaluation/Session1-Modern-LLM-Foundations/instructor/Session1_Instructor_LLM_Foundations.ipynb", "Task 1"): {
        "conducting": (
            "Start by verifying everyone's API key is working before diving in. "
            "Give students 5-7 minutes. Walk the room and help anyone with environment issues first -- "
            "this is their first API call, so unblock quickly. After time is up, live-code the solution "
            "and emphasize the try/except pattern for production robustness."
        ),
        "mistakes": [
            "Forgetting to set `OPENAI_API_KEY` as an environment variable (most common Day 1 blocker)",
            "Hardcoding the API key directly in the notebook instead of using `os.environ`",
            "Not handling exceptions -- students often skip try/except and get unreadable stack traces",
            "Confusing `response` (the full API object) with `response.choices[0].message.content` (the actual text)",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- this is the first API call. Every subsequent task depends on students having a working connection. Do NOT skip.",
    },
    ("Day1-Foundations-Prompting-Evaluation/Session1-Modern-LLM-Foundations/instructor/Session1_Instructor_LLM_Foundations.ipynb", "Task 2"): {
        "conducting": (
            "Give students 8-10 minutes. This task has more logic than Task 1. "
            "Suggest students start by just counting tokens (Step 1-2) before implementing truncation. "
            "After the exercise, discuss edge cases: What if the prompt has no periods? What about very long single sentences? "
            "Use this as a bridge to explain why context window management matters for RAG on Day 3."
        ),
        "mistakes": [
            "Using `len(prompt.split())` (word count) instead of `tiktoken` for token counting -- emphasize that tokens != words",
            "Splitting on `'.'` instead of `'. '` which breaks abbreviations like 'U.S.' and decimal numbers like '$2.3B'",
            "Not adding the period back after splitting -- the rebuilt text loses sentence endings",
            "Forgetting to handle the case where the prompt is already under the limit (should return as-is)",
            "Off-by-one errors in the running token count -- not accounting for spaces between reassembled sentences",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. The core concept (tokens != words) can be conveyed verbally using Demo 2. Students will encounter tiktoken again in Day 3 RAG sessions. If skipping, at minimum show the solution and discuss the sentence-boundary truncation idea.",
    },
    ("Day1-Foundations-Prompting-Evaluation/Session1-Modern-LLM-Foundations/instructor/Session1_Instructor_LLM_Foundations.ipynb", "Task 3"): {
        "conducting": (
            "Give students 5-7 minutes. This is a straightforward loop exercise. "
            "Encourage students to try different prompts beyond the provided test to see how temperature "
            "affects creative vs. analytical outputs. After the exercise, ask: 'When would you use temperature=0 "
            "in a consulting context?' (Answer: financial calculations, data extraction, classification) vs. "
            "'When would you use temperature=1.0?' (Answer: brainstorming, creative strategy ideation)."
        ),
        "mistakes": [
            "Setting both `temperature` and `top_p` at the same time -- OpenAI recommends changing only one",
            "Using a dictionary with float keys and then trying to access with `results[0]` instead of `results[0.0]`",
            "Creating a new `openai.OpenAI()` client inside the loop (wasteful but not incorrect -- discuss efficiency)",
            "Not returning the results dictionary -- just printing inside the function",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. The concept is already well-demonstrated in Demo 3. If skipping, briefly show the solution and move directly to Task 4 which is more important for Day 2 foundations.",
    },
    ("Day1-Foundations-Prompting-Evaluation/Session1-Modern-LLM-Foundations/instructor/Session1_Instructor_LLM_Foundations.ipynb", "Task 4"): {
        "conducting": (
            "Give students 10-12 minutes -- this is the most important task of Session 1. "
            "Suggest building incrementally: first get `__init__` working with the system message, then `chat()` with "
            "a single turn, then verify multi-turn context retention. The key 'aha moment' is when the second question "
            "references context from the first turn and the model remembers. Walk through the message history at the end "
            "to show students exactly what the model receives. This pattern is the foundation for everything in Day 2."
        ),
        "mistakes": [
            "Not including the system message in the initial `self.messages` list -- the persona never takes effect",
            "Appending only the user message but forgetting to append the assistant's response -- context is lost after each turn",
            "Sending only the latest message instead of the full `self.messages` history -- destroys multi-turn memory",
            "Initializing `self.client = openai.OpenAI()` outside `__init__` at the class level (works but is fragile)",
            "Returning `response` instead of `response.choices[0].message.content` from the `chat()` method",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- this introduces the conversational agent pattern (system message + history management) that is the foundation for every agent built on Days 2 and 3. Do NOT skip.",
    },

    # =========== DAY 1 SESSION 2 ===========
    ("Day1-Foundations-Prompting-Evaluation/Session2-Prompt-Engineering/instructor/Session2_Instructor_Prompt_Engineering.ipynb", "Task 1"): {
        "conducting": (
            "Give students 8-10 minutes. Encourage them to draft the system prompt in a text editor first before coding. "
            "The key teaching point is that a well-structured system prompt (100-300 words) with explicit output format "
            "instructions dramatically improves response quality. After the exercise, compare 2-3 student system prompts "
            "and discuss what makes one more effective than another. Ask: 'What happens if you remove the output format section?'"
        ),
        "mistakes": [
            "Writing a system prompt that is too vague ('You are a helpful assistant') -- needs specific persona and constraints",
            "Not specifying the output format explicitly -- the model returns unstructured prose instead of sections",
            "Making the system prompt too long (500+ words) which wastes tokens and can confuse the model",
            "Forgetting to include the system message in the `messages` list (only sending the user message)",
            "Not testing with different questions -- the prompt may work for one query but fail for others",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- system prompt design is the single most important prompting skill. Every agent on Days 2-3 depends on well-crafted system prompts. Do NOT skip.",
    },
    ("Day1-Foundations-Prompting-Evaluation/Session2-Prompt-Engineering/instructor/Session2_Instructor_Prompt_Engineering.ipynb", "Task 2"): {
        "conducting": (
            "Give students 10-12 minutes. Walk through the ReAct pattern on the whiteboard first: "
            "Thought -> Action -> Observation -> repeat. Emphasize that the LLM is *simulating* tool use here -- "
            "the actions are not actually executed. This builds intuition for real tool calling in Day 2 Session 1. "
            "After the exercise, show how the same pattern works with real function calling (preview of Day 2)."
        ),
        "mistakes": [
            "Not defining the available actions clearly in the system prompt -- the model invents its own tools",
            "Confusing the ReAct format with chain-of-thought -- ReAct requires explicit Action and Observation steps",
            "Setting max_tokens too low and the model gets cut off mid-reasoning",
            "Students may not understand that Observation is simulated by the LLM, not real data -- clarify this is a prompting pattern",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. The ReAct concept is demonstrated in Demo 4 and will be implemented properly with real tools in Day 2 Session 3 (LangGraph). If skipping, briefly explain the Thought/Action/Observation cycle verbally and move to Task 3.",
    },
    ("Day1-Foundations-Prompting-Evaluation/Session2-Prompt-Engineering/instructor/Session2_Instructor_Prompt_Engineering.ipynb", "Task 3"): {
        "conducting": (
            "Give students 8-10 minutes. This is a good exercise for students comfortable with Python classes. "
            "Suggest starting with the `__init__` and `format()` method first, then adding `validate()`. "
            "After the exercise, discuss how prompt templates prevent prompt injection and ensure consistency "
            "across an engagement team. Show how LangChain's `ChatPromptTemplate` (Day 2) does the same thing."
        ),
        "mistakes": [
            "Using Python f-strings instead of a proper template system -- f-strings evaluate immediately, templates are deferred",
            "Not using `re.findall(r'\\{(\\w+)\\}', template)` to extract variable names -- students manually list them",
            "Forgetting to validate that all required variables are provided before calling format()",
            "Returning the template class instead of the formatted string from `.format()`",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. LangChain's `ChatPromptTemplate` (Day 2 Session 2) provides the same functionality out-of-the-box. If skipping, briefly show one template example and explain that LangChain handles this natively.",
    },
    ("Day1-Foundations-Prompting-Evaluation/Session2-Prompt-Engineering/instructor/Session2_Instructor_Prompt_Engineering.ipynb", "Task 4"): {
        "conducting": (
            "Give students 12-15 minutes -- this is the session's capstone task. "
            "This is the most complex exercise so far. Suggest a phased approach: "
            "(1) Define the tool descriptions in the system prompt, (2) Get one tool call working with JSON parsing, "
            "(3) Add the loop. Walk the room actively -- students will struggle with JSON parsing. "
            "After the exercise, connect this to Day 2: 'Tomorrow you'll build this same pattern using OpenAI function calling "
            "and LangGraph, which handle the JSON parsing and loop for you.'"
        ),
        "mistakes": [
            "The LLM output not being valid JSON -- students need `response_format={'type': 'json_object'}` or robust parsing",
            "Infinite loops when the model never outputs 'final_answer' as the tool name -- always add a max_steps limit",
            "Not including simulated tool results in the conversation history -- the model loses context of what it already did",
            "Hardcoding tool responses instead of building a proper dispatch mechanism",
            "Forgetting to handle the case where the model responds directly without calling any tool",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- this is the capstone that ties together system prompts, structured output, and multi-step reasoning. It directly previews the agentic patterns students will build with proper frameworks on Day 2. Do NOT skip.",
    },

    # =========== DAY 2 SESSION 1 ===========
    ("Day2-LangChain-LangGraph-Multi-Agent/Session1-OpenAI-API-Structured-Outputs/instructor/Session1_Instructor_OpenAI_API_Structured_Outputs.ipynb", "Task 1"): {
        "conducting": (
            "Give students 8-10 minutes. Remind them to include 'JSON' in the prompt when using "
            "`response_format={'type': 'json_object'}`. Suggest they define the expected schema in the system prompt "
            "before writing code. After the exercise, discuss: 'What happens if the briefing text doesn't mention any "
            "executives? How does your code handle empty lists?'"
        ),
        "mistakes": [
            "Forgetting to include the word 'JSON' in the system or user message -- OpenAI requires this when using JSON mode",
            "Not using `json.loads()` to parse the response -- treating the raw string as a dictionary",
            "Expecting exact field names without specifying them in the system prompt -- the model may use different keys",
            "Not handling the case where a category is empty (no executives mentioned) -- should return an empty list, not omit the key",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- JSON mode is the foundation for all structured outputs. Tasks 2-4 all build on this. Do NOT skip.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session1-OpenAI-API-Structured-Outputs/instructor/Session1_Instructor_OpenAI_API_Structured_Outputs.ipynb", "Task 2"): {
        "conducting": (
            "Give students 10-12 minutes. This is the first time students implement the full function-calling loop. "
            "Draw the flow on the board: User -> Model (tool_call) -> Execute function -> Send result back -> Model (final answer). "
            "Walk through Demo 3 again if students are confused. The key insight is that function calling is a *protocol* -- "
            "the model doesn't actually call your function, it tells you what to call."
        ),
        "mistakes": [
            "Not checking `message.tool_calls` before trying to access tool call properties -- causes AttributeError",
            "Forgetting to send the tool result back to the model for the final answer -- just returning raw simulated data",
            "Using the wrong `tool_call_id` when sending results back -- must match the ID from the model's response",
            "Defining the function schema with incorrect `enum` values that don't match what the function actually handles",
            "Not including the original `message` (with tool_calls) in the follow-up messages list",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- function calling is the core mechanism for tool-using agents. Days 2-3 depend heavily on this pattern. Do NOT skip.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session1-OpenAI-API-Structured-Outputs/instructor/Session1_Instructor_OpenAI_API_Structured_Outputs.ipynb", "Task 3"): {
        "conducting": (
            "Give students 10-12 minutes. Emphasize the dispatch dictionary pattern -- it's cleaner than if/elif chains. "
            "Students should implement the tool functions first (simulated data), then the dispatch table, then the agent loop. "
            "After the exercise, ask: 'What would you need to change to add a fourth tool?' (Answer: one function + one schema + one dispatch entry). "
            "This extensibility is why the dispatch pattern matters."
        ),
        "mistakes": [
            "Using if/elif chains instead of a dispatch dictionary -- works but doesn't scale and is error-prone",
            "Mismatching the function name in the tool schema vs. the dispatch dictionary key",
            "Not handling the case where the model calls multiple tools in one response (parallel tool calls)",
            "Forgetting to convert `json.loads(tc.function.arguments)` -- passing the raw string to the function",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. This extends Task 2 with multiple tools but the core pattern is the same. If skipping, show the dispatch dictionary concept briefly and move to Task 4. Students will see multi-tool patterns again in Day 2 Session 2 with LangChain.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session1-OpenAI-API-Structured-Outputs/instructor/Session1_Instructor_OpenAI_API_Structured_Outputs.ipynb", "Task 4"): {
        "conducting": (
            "Give students 12-15 minutes -- this is the session capstone. Suggest building in layers: "
            "(1) Basic call without retries, (2) Add retry logic, (3) Add Pydantic validation, (4) Add streaming. "
            "Not all students will finish all four features -- that's OK. Prioritize retries and validation. "
            "After the exercise, discuss production concerns: rate limits, cost tracking, graceful degradation."
        ),
        "mistakes": [
            "Implementing retries with a fixed delay instead of exponential backoff (`2 ** attempt`)",
            "Catching all exceptions in the retry loop instead of only retryable ones (rate limits, timeouts)",
            "Not tracking token usage from streaming responses (streaming doesn't return usage by default)",
            "Using `model_validate()` instead of `model_validate_json()` -- the response is a JSON string, not a dict",
            "Forgetting to accumulate `total_prompt_tokens` and `total_completion_tokens` across calls",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. The individual concepts (retries, Pydantic, streaming) are all demonstrated in the demos. If skipping, walk through the solution code highlighting the retry pattern and Pydantic validation -- these are the most production-relevant pieces.",
    },

    # =========== DAY 2 SESSION 2 ===========
    ("Day2-LangChain-LangGraph-Multi-Agent/Session2-LangChain-Tool-Integration/instructor/Session2_Instructor_LangChain_Tool_Integration.ipynb", "Task 1"): {
        "conducting": (
            "Give students 8-10 minutes. This is students' first LCEL chain. "
            "Write the pipe syntax on the board: `prompt | llm | parser`. "
            "Emphasize that LCEL is just Python's `|` operator overloaded for composition. "
            "Suggest starting with `StrOutputParser` first, then switching to `JsonOutputParser`. "
            "After the exercise, discuss why JSON output is important for downstream processing in agentic systems."
        ),
        "mistakes": [
            "Forgetting to import `JsonOutputParser` from `langchain_core.output_parsers`",
            "Not including 'JSON' or format instructions in the prompt -- the model returns prose instead of JSON",
            "Calling `chain.run()` (old API) instead of `chain.invoke()` (LCEL API)",
            "Passing a string instead of a dictionary to `chain.invoke()` when the prompt has multiple variables",
            "Not understanding that `|` creates a new chain object -- it doesn't modify in place",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- LCEL is the foundation for all LangChain chains. Every subsequent task and Day 3 RAG pipeline uses this pattern. Do NOT skip.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session2-LangChain-Tool-Integration/instructor/Session2_Instructor_LangChain_Tool_Integration.ipynb", "Task 2"): {
        "conducting": (
            "Give students 8-10 minutes. Walk through the `@tool` decorator syntax from Demo 3. "
            "Suggest students implement one tool first, test it, then add the other two. "
            "After the exercise, show `llm_with_tools.invoke()` and discuss how the model decides which tool to call. "
            "Ask: 'What happens if a query doesn't match any tool?' (Answer: the model responds directly without calling tools)."
        ),
        "mistakes": [
            "Not adding docstrings to `@tool` decorated functions -- LangChain uses the docstring as the tool description for the LLM",
            "Incorrect type annotations on tool parameters -- LangChain infers the schema from type hints",
            "Returning complex objects instead of strings from tools -- tool outputs must be serializable",
            "Trying to call `tool.invoke()` directly instead of letting the LLM decide when to use the tool",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. The `@tool` pattern is well-covered in Demo 3. If skipping, briefly show one custom tool and how `bind_tools()` works, then move to Task 3 (memory) which is more foundational for agents.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session2-LangChain-Tool-Integration/instructor/Session2_Instructor_LangChain_Tool_Integration.ipynb", "Task 3"): {
        "conducting": (
            "Give students 10-12 minutes. This is conceptually important -- it bridges Session 1's SimpleAgent "
            "to LangChain's memory system. Emphasize that `MessagesPlaceholder('history')` is where prior turns get injected. "
            "Suggest students get a single-turn response working first, then add the history list and multi-turn. "
            "After the exercise, test with 3+ turns to show the model remembering context."
        ),
        "mistakes": [
            "Forgetting `MessagesPlaceholder('history')` in the prompt template -- the history is never injected",
            "Passing `self.history` as a string instead of a list of `HumanMessage`/`AIMessage` objects",
            "Appending `HumanMessage` but forgetting to append `AIMessage` -- the model loses assistant context",
            "Using `ChatPromptTemplate.from_template()` (single template) instead of `ChatPromptTemplate.from_messages()` (message list)",
            "Not passing `{'history': self.history, ...}` to `chain.invoke()` -- the history variable is missing",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- conversation memory is essential for multi-turn agents. Day 2 Sessions 3-4 and Day 3 all assume students understand this pattern. Do NOT skip.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session2-LangChain-Tool-Integration/instructor/Session2_Instructor_LangChain_Tool_Integration.ipynb", "Task 4"): {
        "conducting": (
            "Give students 10-12 minutes. This is a preview of Day 3's full RAG session. "
            "Walk students through the retrieve-then-generate pattern. "
            "The keyword-overlap scoring is intentionally simple -- tell students: 'On Day 3 you'll replace this "
            "with embedding-based semantic search, but the retrieve -> generate architecture stays the same.' "
            "Focus on the RAG chain composition with LCEL."
        ),
        "mistakes": [
            "Implementing retrieval as a simple string match instead of keyword overlap scoring",
            "Not including source metadata in the context passed to the LLM -- the model can't cite sources",
            "Returning raw chunks without any formatting -- the LLM needs clearly separated context pieces",
            "Setting `chunk_overlap=0` which causes information loss at chunk boundaries",
            "Not testing with queries that span multiple documents to verify retrieval quality",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. This is a simplified preview of Day 3 Session 1 (full RAG). If skipping, explain the retrieve-then-generate concept verbally with a diagram and tell students they will build a proper version tomorrow with embeddings and ChromaDB.",
    },

    # =========== DAY 2 SESSION 3 ===========
    ("Day2-LangChain-LangGraph-Multi-Agent/Session3-LangGraph-Orchestration/instructor/Session3_Instructor_LangGraph_Orchestration.ipynb", "Task 1"): {
        "conducting": (
            "Give students 8-10 minutes. This is students' first LangGraph StateGraph. "
            "Draw the linear graph on the board: START -> gather_data -> analyze_situation -> prepare_brief -> END. "
            "Emphasize the TypedDict state pattern -- each node reads from and writes to the shared state. "
            "After the exercise, run the graph and inspect the state at each step to build intuition."
        ),
        "mistakes": [
            "Defining the state TypedDict without proper type annotations -- LangGraph requires typed fields",
            "Forgetting `graph.set_entry_point()` and `graph.set_finish_point()` -- the graph has no start/end",
            "Adding edges in the wrong order or creating cycles in what should be a linear pipeline",
            "Not returning the updated state dictionary from each node function -- state changes are lost",
            "Calling `graph.compile()` but not `graph.invoke()` -- students think compilation runs the graph",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- this is the first LangGraph exercise. The StateGraph, TypedDict, and node pattern are required for all subsequent tasks and Day 3 capstones. Do NOT skip.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session3-LangGraph-Orchestration/instructor/Session3_Instructor_LangGraph_Orchestration.ipynb", "Task 2"): {
        "conducting": (
            "Give students 10-12 minutes. Draw the conditional routing diagram on the board: "
            "classify -> (if quick) quick_screen, (if standard) standard_diligence, (if deep) deep_dive -> END. "
            "Emphasize that `add_conditional_edges` takes a routing function that returns a string matching the node names. "
            "The most common confusion is the routing function return values -- they must exactly match registered node names."
        ),
        "mistakes": [
            "The routing function returning strings that don't match any registered node name -- causes a runtime error",
            "Forgetting to add the conditional edge from the classify node -- only adding regular edges",
            "Not making the LLM return a structured classification (e.g., just one word) -- parsing long-form responses is fragile",
            "Adding edges from conditional target nodes back to the classifier, creating an unintended loop",
            "Using `add_edge` where `add_conditional_edges` is needed -- all paths go to the same node",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- conditional routing is the core pattern for intelligent agents that make decisions. Day 2 Session 4 and both Day 3 capstones heavily use conditional edges. Do NOT skip.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session3-LangGraph-Orchestration/instructor/Session3_Instructor_LangGraph_Orchestration.ipynb", "Task 3"): {
        "conducting": (
            "Give students 10-12 minutes. This introduces cycles -- draw the loop on the board: "
            "generate -> assess_quality -> (if not MECE, loop back to generate) or (if MECE, go to END). "
            "Emphasize the `attempts` counter and max_attempts guard to prevent infinite loops. "
            "After the exercise, ask: 'What would happen without the max_attempts limit?' "
            "This is a critical design pattern for self-correcting agents."
        ),
        "mistakes": [
            "Creating an infinite loop by not incrementing the `attempts` counter or not checking it in the routing function",
            "The quality assessment always returning 'pass' or 'fail' regardless of actual content -- check the LLM prompt",
            "Not passing the previous feedback back to the generation node -- the model regenerates without knowing what to fix",
            "Setting max_attempts too high (>5) -- wastes API calls and time during class",
            "Forgetting the exit condition in the routing function -- the graph never terminates",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. Cycles are demonstrated in Demo 4. If skipping, walk through the solution briefly emphasizing the loop + exit condition pattern, and move to Task 4. Students will encounter cycles again in Day 3 Track B Milestone 4 (partner review loop).",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session3-LangGraph-Orchestration/instructor/Session3_Instructor_LangGraph_Orchestration.ipynb", "Task 4"): {
        "conducting": (
            "Give students 12-15 minutes -- this is the session capstone. "
            "This combines linear, conditional, and cyclic patterns. Suggest building in stages: "
            "(1) scope_assessment node, (2) execute_workstream + check_progress loop, (3) synthesize_recommendation. "
            "Walk the room actively -- students will struggle with the loop that processes workstreams one at a time. "
            "After the exercise, discuss how this mirrors a real consulting engagement structure."
        ),
        "mistakes": [
            "Trying to process all workstreams in a single node instead of looping through them one at a time",
            "The check_progress routing function not correctly tracking which workstreams are completed",
            "Not accumulating findings across workstream iterations -- each loop overwrites previous findings",
            "The scope_assessment generating too many workstreams (5+) -- instruct the LLM to limit to 2-3",
            "JSON parsing failures when the LLM's workstream plan isn't valid JSON -- add error handling",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running significantly behind schedule. This is an advanced exercise combining all LangGraph patterns. If skipping, walk through the solution code and diagram the graph structure on the board. Ensure students understand the concept even if they don't implement it.",
    },

    # =========== DAY 2 SESSION 4 ===========
    ("Day2-LangChain-LangGraph-Multi-Agent/Session4-Multi-Agent-Workflows/instructor/Session4_Instructor_Multi_Agent_Workflows.ipynb", "Task 1"): {
        "conducting": (
            "Give students 10-12 minutes. Draw the supervisor-worker pattern on the board: "
            "Supervisor -> (quantitative OR strategic) -> Partner Review -> END. "
            "Emphasize that the supervisor is just an LLM node that classifies and routes -- it doesn't do the work. "
            "After the exercise, compare the supervisor pattern to Session 3's conditional routing and discuss when to use each."
        ),
        "mistakes": [
            "The supervisor node doing the actual analysis instead of just classifying and routing",
            "Routing function returning 'analyst' when the node is registered as 'quantitative_associate' -- name mismatch",
            "Not including the partner review step -- the worker output goes directly to END without quality check",
            "Students confusing the supervisor's classification prompt with the worker's analysis prompt",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- the supervisor-worker pattern is one of the two core multi-agent architectures (along with handoff). Both Day 3 capstones use variations of this pattern. Do NOT skip.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session4-Multi-Agent-Workflows/instructor/Session4_Instructor_Multi_Agent_Workflows.ipynb", "Task 2"): {
        "conducting": (
            "Give students 10-12 minutes. The key concept is the `handoff_context` field in the state "
            "that accumulates notes as work passes between agents. Draw the pipeline: "
            "Research Associate -> Industry Expert -> Partner Synthesis, with an arrow showing context flowing forward. "
            "After the exercise, discuss: 'What information should be in the handoff? What should NOT be?'"
        ),
        "mistakes": [
            "Not accumulating `handoff_context` -- each agent overwrites instead of appending to the previous context",
            "Agent B not receiving the output of Agent A -- forgetting to include prior agent output in the prompt",
            "Making the handoff_context too verbose (dumping full outputs) instead of summarizing key findings",
            "All three agents using the same system prompt -- they should have distinct personas and expertise areas",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. The handoff concept is well-demonstrated in Demo 2. If skipping, show the solution briefly and emphasize the handoff_context accumulation pattern. Task 3 (parallel execution) is more novel and should be prioritized.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session4-Multi-Agent-Workflows/instructor/Session4_Instructor_Multi_Agent_Workflows.ipynb", "Task 3"): {
        "conducting": (
            "Give students 10-12 minutes. Explain that 'parallel' here means fan-out/fan-in: "
            "multiple agents process independently, then a synthesis agent combines their outputs. "
            "In LangGraph these run sequentially but the key insight is they are *independent* -- no agent needs another's output. "
            "After the exercise, discuss: 'How would you make these truly parallel in production?' (Answer: async, threading, or distributed execution)."
        ),
        "mistakes": [
            "Making agents dependent on each other's output (sequential) instead of independent (parallel-ready)",
            "The synthesis agent not receiving ALL three agent outputs -- only gets the last one",
            "Not storing each agent's output in a separate state field (e.g., `commercial_output`, `supply_chain_output`)",
            "The synthesis just concatenating outputs instead of truly synthesizing them into a coherent narrative",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. This extends the fan-out/fan-in pattern from Demo 3. If skipping, walk through the solution and discuss how fan-out/fan-in differs from sequential handoff. The concept appears again in Day 3 Track B capstone.",
    },
    ("Day2-LangChain-LangGraph-Multi-Agent/Session4-Multi-Agent-Workflows/instructor/Session4_Instructor_Multi_Agent_Workflows.ipynb", "Task 4"): {
        "conducting": (
            "Give students 15-20 minutes -- this is the Day 2 capstone and most complex exercise. "
            "Let students choose their own use case or follow the M&A due diligence example. "
            "The key requirements are: 3+ agents, 1+ conditional edge, and a combined output. "
            "Walk the room actively. Many students will need help designing the graph before coding. "
            "After the exercise, have 2-3 students present their architectures to the class."
        ),
        "mistakes": [
            "Starting to code immediately without designing the graph structure on paper first",
            "Creating too many agents (5+) -- the system becomes hard to debug and slow to run",
            "Conditional edges that are never triggered because the routing logic doesn't match actual inputs",
            "Not having a clear 'output' node that combines all agent results into a final deliverable",
            "The state TypedDict growing too large -- each field should serve a clear purpose",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running significantly behind schedule, but try to preserve at least 10 minutes for it. This is the Day 2 capstone. If skipping entirely, walk through the M&A due diligence solution and diagram the architecture. This exercise is important preparation for Day 3 capstones.",
    },

    # =========== DAY 3 SESSION 1 ===========
    ("Day3-RAG-Deployment-Capstone/Session1-Retrieval-Augmented-Generation/instructor/Session1_Instructor_RAG.ipynb", "Task 1"): {
        "conducting": (
            "Give students 10-12 minutes. This is their first time working with embeddings programmatically. "
            "Suggest building in two steps: (1) embed all documents in `__init__`, (2) implement `search()` with cosine similarity. "
            "After the exercise, test with queries that use synonyms to show embedding-based search finds semantically similar content "
            "even when keywords don't match -- this is the key advantage over keyword search."
        ),
        "mistakes": [
            "Not normalizing vectors before computing cosine similarity -- results are incorrect",
            "Computing similarity between query and documents by iterating one-at-a-time instead of vectorized numpy operations",
            "Embedding documents at search time instead of at initialization -- causes redundant API calls and slow search",
            "Returning documents without their similarity scores -- students can't verify the ranking is correct",
            "Using a different embedding model for queries vs. documents -- embeddings must use the same model to be comparable",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- embedding search is the core of RAG. Every subsequent task and both capstones depend on this. Do NOT skip.",
    },
    ("Day3-RAG-Deployment-Capstone/Session1-Retrieval-Augmented-Generation/instructor/Session1_Instructor_RAG.ipynb", "Task 2"): {
        "conducting": (
            "Give students 8-10 minutes. The key teaching point is that different document types "
            "benefit from different chunking strategies. Suggest students implement type detection first, "
            "then map each type to a splitter. After the exercise, discuss: 'Why does chunk size matter? "
            "What happens if chunks are too small? Too large?'"
        ),
        "mistakes": [
            "Using the same splitter for all document types -- defeats the purpose of smart chunking",
            "Setting chunk_size too small (<100 chars) -- chunks lose context and meaning",
            "Setting chunk_overlap to 0 -- information at chunk boundaries is lost",
            "Not detecting document type correctly -- a simple heuristic (look for markdown headers, code patterns) is sufficient",
            "Forgetting to add metadata (type, size) to returned chunks",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. The chunking concept is well-covered in Demo 3. If skipping, briefly explain that different document types need different splitting strategies and show the strategy comparison from the demo. Task 3 (query expansion) is more impactful.",
    },
    ("Day3-RAG-Deployment-Capstone/Session1-Retrieval-Augmented-Generation/instructor/Session1_Instructor_RAG.ipynb", "Task 3"): {
        "conducting": (
            "Give students 10-12 minutes. Walk through the pipeline: expand query into variants -> "
            "retrieve for each variant -> deduplicate -> rerank with LLM. "
            "Emphasize that query expansion catches results that a single phrasing would miss. "
            "After the exercise, compare results with and without expansion to show the improvement."
        ),
        "mistakes": [
            "Not deduplicating results across query variants -- the same chunk appears multiple times",
            "The LLM reranking prompt not returning just a number -- add strict instructions ('Return ONLY a number 0-10')",
            "Expanding into too many variants (5+) -- increases latency and cost without proportional benefit",
            "Not using the original query as one of the variants -- only using the expanded versions",
            "The reranking LLM call failing JSON parsing -- wrap in try/except with a default score",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. Query expansion and reranking are advanced techniques. If skipping, explain the concept verbally and note that the capstone (Session 3A) includes this as Milestone 2, where students will implement it. Move to Task 4 for the end-to-end picture.",
    },
    ("Day3-RAG-Deployment-Capstone/Session1-Retrieval-Augmented-Generation/instructor/Session1_Instructor_RAG.ipynb", "Task 4"): {
        "conducting": (
            "Give students 12-15 minutes -- this is the session capstone. "
            "This task adds evaluation metrics to the RAG pipeline. Suggest implementing `query()` first "
            "to get a working pipeline, then adding `evaluate()`. The three metrics (relevance, faithfulness, completeness) "
            "are scored by LLM-as-judge. After the exercise, discuss: 'Which metric is hardest to score accurately? "
            "How would you validate the judge's scores?'"
        ),
        "mistakes": [
            "The evaluation LLM using the same model that generated the answer -- ideally use a different or larger model as judge",
            "Not structuring the evaluation prompt to return only a number -- the model returns explanations that break parsing",
            "Evaluating retrieval relevance by checking keyword overlap instead of using the LLM judge",
            "Not passing the original question to the faithfulness evaluation -- the judge needs context",
            "Skipping the completeness metric -- this is the hardest but most valuable for consulting quality",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. The evaluation concepts are demonstrated in Demo 5 and Day 1 Session 3. If skipping, walk through the solution focusing on the three evaluation dimensions. Track A capstone (Session 3A) includes evaluation as Milestone 4.",
    },

    # =========== DAY 3 SESSION 2 ===========
    ("Day3-RAG-Deployment-Capstone/Session2-Deployment-Scaling/instructor/Session2_Instructor_Deployment.ipynb", "Task 1"): {
        "conducting": (
            "Give students 8-10 minutes. Draw the sliding window concept on the board: "
            "requests in the last 60 seconds. Suggest using a list of timestamps and pruning old entries. "
            "After the exercise, test by sending rapid requests to trigger the rate limit. "
            "Discuss: 'Why do we need client-side rate limiting when the API already has rate limits?' "
            "(Answer: graceful degradation, cost control, fair usage across teams)."
        ),
        "mistakes": [
            "Using a simple counter instead of a sliding window -- the counter never resets",
            "Not pruning old entries from the tracking list -- the list grows unbounded and checks slow down",
            "Checking only RPM (requests per minute) but not TPM (tokens per minute) -- both matter",
            "Blocking requests silently instead of returning a helpful error message with retry-after info",
            "Using `time.time()` incorrectly -- comparing timestamps across different time zones or formats",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. Rate limiting is a production concern well-covered in Demo 1. If skipping, explain the concept verbally and note that Task 4 (LLM Gateway) combines rate limiting with other features. Move to Task 2 (streaming) which is more hands-on.",
    },
    ("Day3-RAG-Deployment-Capstone/Session2-Deployment-Scaling/instructor/Session2_Instructor_Deployment.ipynb", "Task 2"): {
        "conducting": (
            "Give students 8-10 minutes. The key metric is TTFT (time-to-first-token). "
            "Show students how to use `stream=True` with the OpenAI API and iterate over chunks. "
            "After the exercise, discuss: 'Why does streaming matter for consulting AI?' "
            "(Answer: partners don't want to wait 10 seconds staring at a blank screen for a CEO briefing)."
        ),
        "mistakes": [
            "Not setting `stream=True` in the API call -- gets a complete response instead of streaming",
            "Measuring TTFT incorrectly -- should be time from request start to first non-empty chunk",
            "Not handling `None` content in delta chunks -- causes AttributeError when checking `.content`",
            "Forgetting to collect the full response while streaming -- only printing chunks without accumulating",
            "Not calculating tokens-per-second correctly -- dividing total tokens by total time instead of streaming time",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. Streaming is demonstrated in Day 2 Session 1 Demo 1. If skipping, briefly show the TTFT concept and move to Task 3 (caching) which is more impactful for production systems.",
    },
    ("Day3-RAG-Deployment-Capstone/Session2-Deployment-Scaling/instructor/Session2_Instructor_Deployment.ipynb", "Task 3"): {
        "conducting": (
            "Give students 10-12 minutes. Draw the three-tier cache diagram on the board: "
            "Exact match (dict) -> Semantic match (embeddings) -> LLM call. "
            "Emphasize that each tier has different tradeoffs: speed vs. flexibility. "
            "After the exercise, test with three queries: exact duplicate, semantically similar, and completely new. "
            "The cache should serve the first two without an LLM call."
        ),
        "mistakes": [
            "Using the raw query string as the exact cache key without normalization (lowercase, strip whitespace)",
            "Setting the semantic similarity threshold too low (0.7) -- returns false matches, or too high (0.99) -- never matches",
            "Not embedding the query for semantic comparison -- just doing string similarity",
            "Caching error responses -- a failed LLM call should not be cached",
            "Not tracking which tier served the response -- makes it impossible to analyze cache effectiveness",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL for Track A capstone -- Milestone 4 requires caching as part of the production wrapper. Also valuable for understanding production AI systems. If truly pressed for time, simplify to just exact + LLM tiers (skip semantic tier).",
    },
    ("Day3-RAG-Deployment-Capstone/Session2-Deployment-Scaling/instructor/Session2_Instructor_Deployment.ipynb", "Task 4"): {
        "conducting": (
            "Give students 12-15 minutes -- this is the session capstone. "
            "This combines all previous concepts: routing, caching, rate limiting, monitoring, cost tracking. "
            "Suggest students compose existing demo/task components rather than building from scratch. "
            "After the exercise, run the dashboard and discuss what metrics an engagement team would monitor. "
            "This directly prepares students for Track A Milestone 4."
        ),
        "mistakes": [
            "Building everything from scratch instead of composing existing components -- this is a composition exercise",
            "Not checking the cache BEFORE making the LLM call -- defeats the purpose of caching",
            "Rate limiting applied after the LLM call instead of before -- the API call is already made",
            "The dashboard returning raw data instead of computed metrics (hit rate, avg latency, cost per query)",
            "Not tracking per-model costs when routing between gpt-4o-mini and gpt-4o",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. This is a composition exercise -- if students understood Tasks 1-3, they understand the components. If skipping, walk through the solution architecture and emphasize the composition pattern. Track A capstone Milestone 4 covers similar ground.",
    },

    # =========== DAY 3 SESSION 3A (Track A Capstone) ===========
    ("Day3-RAG-Deployment-Capstone/Session3-Capstone-Labs/track-a-production-rag/instructor/Session3A_Instructor_Production_RAG.ipynb", "Milestone 1"): {
        "conducting": (
            "Give students 15-20 minutes. This is the foundation for their entire capstone. "
            "Walk through the requirements: chunking with RecursiveCharacterTextSplitter, batch embedding, ChromaDB storage with metadata. "
            "Suggest students test with 2-3 documents first before processing all 5. "
            "Help anyone stuck on ChromaDB setup immediately -- if ingestion doesn't work, nothing else will."
        ),
        "mistakes": [
            "Not batch-embedding chunks (calling the API one chunk at a time) -- very slow for large document sets",
            "Forgetting to pass metadata to ChromaDB's `.add()` -- the metadata is lost and retrieval can't filter by practice area",
            "Using duplicate chunk IDs -- ChromaDB silently overwrites, causing data loss",
            "Setting chunk_size too large (1000+) -- reduces retrieval precision; too small (<100) -- loses context",
            "Not handling the case where a document is shorter than chunk_size -- should produce a single chunk",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- this is Milestone 1. Everything else builds on it. If students are truly stuck, provide the solution code and let them focus on Milestones 2-4.",
    },
    ("Day3-RAG-Deployment-Capstone/Session3-Capstone-Labs/track-a-production-rag/instructor/Session3A_Instructor_Production_RAG.ipynb", "Milestone 2"): {
        "conducting": (
            "Give students 15-20 minutes. Emphasize the three steps: expand, retrieve, rerank. "
            "Suggest students get basic retrieval working first (query ChromaDB directly), then add expansion and reranking. "
            "The reranking step is optional if time is short -- basic retrieval still produces useful results. "
            "After the milestone, test with consulting questions that could be phrased multiple ways."
        ),
        "mistakes": [
            "Not using Milestone 1's collection object -- creating a new empty collection instead",
            "Query expansion generating queries that are too different from the original -- add 'variations of the same question' in the prompt",
            "Reranking all candidates individually (N LLM calls) instead of batch scoring -- very slow for large result sets",
            "Not deduplicating chunks that appear in multiple query variant results",
            "The rerank score parser failing on 'Score: 8/10' format -- instruct the LLM to return ONLY a number",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- retrieval quality directly determines the final answer quality. However, if pressed for time, students can implement basic ChromaDB retrieval without expansion/reranking and still have a working system. Skip expansion and reranking, not the entire milestone.",
    },
    ("Day3-RAG-Deployment-Capstone/Session3-Capstone-Labs/track-a-production-rag/instructor/Session3A_Instructor_Production_RAG.ipynb", "Milestone 3"): {
        "conducting": (
            "Give students 15-20 minutes. The key teaching point is source citations. "
            "Show students how to format context with [Source: doc_name] tags so the LLM can cite them. "
            "Emphasize the low-confidence detection pattern -- if the knowledge base doesn't have an answer, "
            "the system should say so rather than hallucinate. Test with an out-of-scope question to demonstrate."
        ),
        "mistakes": [
            "Not including source information in the context -- the LLM can't cite what it doesn't see",
            "The system prompt not explicitly requiring citations -- the model skips them unless instructed",
            "Low-confidence detection that is too aggressive (flags everything) or too lenient (flags nothing)",
            "Generating answers that go far beyond the provided context -- the system prompt must constrain to context-only",
            "Not testing with a question the knowledge base can't answer -- students miss the confidence flagging feature",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- generation with citations is the core output of the RAG system. Without this, the capstone demo won't show useful results. Do NOT skip.",
    },
    ("Day3-RAG-Deployment-Capstone/Session3-Capstone-Labs/track-a-production-rag/instructor/Session3A_Instructor_Production_RAG.ipynb", "Milestone 4"): {
        "conducting": (
            "Give students 15-20 minutes. This is the integration milestone -- composing Milestones 1-3 plus caching and evaluation. "
            "Suggest students get the basic pipeline working first (ingest -> retrieve -> generate), then add caching, "
            "then evaluation metrics. The dashboard is nice-to-have but not critical for the demo. "
            "Prepare students: 'You'll demo this in Session 4 -- make sure you have a working pipeline with at least one impressive query.'"
        ),
        "mistakes": [
            "Re-implementing components from scratch instead of instantiating Milestone 1-3 classes",
            "Cache check happening after the LLM call instead of before -- no actual caching benefit",
            "Evaluation running on every query -- very slow. Consider making it optional or sampling",
            "The dashboard not computing derived metrics (cache hit rate, avg quality) -- just showing raw logs",
            "Not testing with a duplicate query to verify caching is working",
        ],
        "skippable": True,
        "skip_reason": "CAN SIMPLIFY if running behind schedule. The core value is composing Milestones 1-3 into a working pipeline. Students can skip caching and evaluation and still have a demonstrable system. Prioritize getting the ingest-retrieve-generate flow working end-to-end for the Session 4 demo.",
    },

    # =========== DAY 3 SESSION 3B (Track B Capstone) ===========
    ("Day3-RAG-Deployment-Capstone/Session3-Capstone-Labs/track-b-multi-agent/instructor/Session3B_Instructor_Multi_Agent.ipynb", "Milestone 1"): {
        "conducting": (
            "Give students 15-20 minutes. This agent takes a complex question and decomposes it into workstreams. "
            "Emphasize that the LLM should return structured JSON with workstream details. "
            "Suggest testing with a simple question first ('Should we enter the Indian market?') before complex PE scenarios. "
            "The key quality measure: are the workstreams MECE and do they cover the question comprehensively?"
        ),
        "mistakes": [
            "The LLM not returning valid JSON -- use `response_format={'type': 'json_object'}` or add explicit JSON instructions",
            "Workstreams that overlap (not MECE) -- instruct the LLM to make them mutually exclusive",
            "Too many workstreams (5+) -- each one requires a specialist agent, so 2-4 is ideal for class time",
            "Not including dependencies between workstreams -- some naturally depend on others' outputs",
            "Hardcoding workstreams instead of letting the LLM decompose dynamically based on the question",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- this is the entry point for the entire multi-agent system. If the EM agent doesn't produce good workstreams, the specialist agents have nothing to work on. Do NOT skip.",
    },
    ("Day3-RAG-Deployment-Capstone/Session3-Capstone-Labs/track-b-multi-agent/instructor/Session3B_Instructor_Multi_Agent.ipynb", "Milestone 2"): {
        "conducting": (
            "Give students 15-20 minutes. Students need to implement 4 agent classes with distinct personas. "
            "Suggest a pattern: copy one agent class, then customize the system prompt and output format for each specialist. "
            "Emphasize that each agent should receive context from completed workstreams so they can build on each other's findings. "
            "If time is short, students can implement 2 agents and hardcode the other 2."
        ),
        "mistakes": [
            "All agents using the same generic system prompt -- they should have distinct expertise and frameworks",
            "Not passing cross-workstream context to agents -- they can't reference other agents' findings",
            "Agent output format varying wildly -- standardize on a common structure (result text + metadata dict)",
            "System prompts that are too long (500+ words) -- keep them focused on the agent's specific expertise",
            "Not mapping specialist names to agent classes -- the dispatcher won't know which agent to invoke",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- the specialist agents are the workers in the multi-agent system. Without them, the orchestration (Milestone 3) has nothing to run. If pressed for time, implement 2 agents fully and stub the other 2 with simple LLM calls.",
    },
    ("Day3-RAG-Deployment-Capstone/Session3-Capstone-Labs/track-b-multi-agent/instructor/Session3B_Instructor_Multi_Agent.ipynb", "Milestone 3"): {
        "conducting": (
            "Give students 20-25 minutes -- this is the most complex milestone. "
            "Draw the full graph on the board: EM -> Dispatcher -> Specialist -> (loop back to Dispatcher if more workstreams) -> Synthesis. "
            "The dispatcher node is the key: it picks the next workstream and routes to the right specialist. "
            "Suggest getting the EM -> Dispatcher -> one Specialist -> Synthesis linear path working first, then adding the loop."
        ),
        "mistakes": [
            "The dispatcher not correctly tracking `current_workstream_idx` -- it processes the same workstream repeatedly",
            "Conditional routing returning node names that don't match registered names",
            "Not storing completed workstream results in the state -- the synthesis node has nothing to combine",
            "The loop condition checking the wrong field -- should check if all workstreams are processed",
            "Forgetting to increment `current_workstream_idx` after each specialist execution",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- this is the core of the capstone. Without orchestration, it's just individual agents, not a multi-agent system. If students are really stuck, provide the graph structure code and let them focus on the node logic.",
    },
    ("Day3-RAG-Deployment-Capstone/Session3-Capstone-Labs/track-b-multi-agent/instructor/Session3B_Instructor_Multi_Agent.ipynb", "Milestone 4"): {
        "conducting": (
            "Give students 15-20 minutes. This adds a partner review loop -- the deliverable gets scored "
            "and revised if quality is below threshold. Suggest students implement the review node first, "
            "test it, then add the revision node and loop. Use a threshold of 3.5 average across 3 criteria. "
            "Prepare students: 'You'll demo this in Session 4 -- show the review scores improving across iterations.'"
        ),
        "mistakes": [
            "The partner review always giving high scores (>4) so the loop never triggers -- make the criteria strict",
            "The revision node not knowing which criterion was weakest -- pass the scores and identify the lowest",
            "No max revision limit -- the loop runs indefinitely if quality never reaches the threshold",
            "Not tracking scores across iterations -- students can't show improvement in their demo",
            "The revision rewriting the entire deliverable instead of targeting the weakest area",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. Milestones 1-3 produce a working multi-agent system that is demonstrable. The partner review loop is a polish layer. If skipping, students can still demo a functional multi-agent engagement team. Encourage them to mention it as a 'future enhancement' in their presentation.",
    },

    # =========== DAY 3 SESSION 4 ===========
    ("Day3-RAG-Deployment-Capstone/Session4-Debrief-Governance/instructor/Session4_Instructor_Debrief_Governance.ipynb", "Task 1"): {
        "conducting": (
            "Give students 8-10 minutes. This is the first governance exercise. "
            "Suggest students start with 3-4 simple regex rules (block confidential data requests, flag prompt injection attempts). "
            "Emphasize the severity levels: block (stop completely), warn (allow but log), allow (pass through). "
            "After the exercise, test with both safe and unsafe queries to verify the guardrails work."
        ),
        "mistakes": [
            "Regex patterns that are too broad -- blocking legitimate consulting queries that happen to mention 'confidential'",
            "Not handling the case where multiple rules match -- should return the highest severity",
            "Only checking input but not output -- the model might generate inappropriate content even with safe inputs",
            "Hardcoding rules instead of loading from a config -- makes the system inflexible",
            "Not logging blocked/warned requests -- audit trail is essential for governance",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- guardrails are the minimum viable governance feature. Every production AI system needs input/output checking. Do NOT skip. This also ties directly to the governance scorecard in Task 3.",
    },
    ("Day3-RAG-Deployment-Capstone/Session4-Debrief-Governance/instructor/Session4_Instructor_Debrief_Governance.ipynb", "Task 2"): {
        "conducting": (
            "Give students 10-12 minutes. This task tests whether the AI treats different demographic groups consistently. "
            "Emphasize that bias testing is not about catching obvious discrimination -- it's about subtle inconsistencies "
            "in recommendation quality or framing. After the exercise, discuss: 'How would you handle it if bias is detected? "
            "What changes to the system prompt or pipeline could mitigate it?'"
        ),
        "mistakes": [
            "Using too few demographic groups (only 2) -- need at least 3-4 for meaningful comparison",
            "Not using the same template structure for all groups -- inconsistent prompts invalidate the comparison",
            "The LLM judge rating consistency instead of quality -- we want to measure if responses are equally good, not identical",
            "Not providing specific examples of detected bias -- just saying 'bias detected' is not actionable",
            "Testing only one dimension (e.g., only gender) -- should test multiple (industry, geography, etc.)",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule. Bias detection is important conceptually but can be discussed verbally. If skipping, show the solution briefly and discuss the concept of fairness testing for AI systems. The governance scorecard (Task 3) references bias testing regardless.",
    },
    ("Day3-RAG-Deployment-Capstone/Session4-Debrief-Governance/instructor/Session4_Instructor_Debrief_Governance.ipynb", "Task 3"): {
        "conducting": (
            "Give students 10-12 minutes. This task connects governance to their capstone project. "
            "Ask students to evaluate their own capstone (Track A or B) against 8 governance criteria. "
            "The key output is identifying the top 3 gaps and proposing specific remediations. "
            "After the exercise, have students share their top gaps -- this creates a rich discussion about AI governance in consulting."
        ),
        "mistakes": [
            "Giving all criteria a score of 5 ('everything is fine') -- be honest about gaps, that's the point",
            "Criteria descriptions that are too generic -- tailor to the specific capstone built today",
            "Not proposing specific, actionable remediations -- 'improve security' is not actionable",
            "Scoring criteria they didn't actually implement in their capstone (e.g., scoring 'audit trail' 4/5 when they have no logging)",
            "Not connecting remediation to the specific weakness -- remediation should directly address the gap",
        ],
        "skippable": False,
        "skip_reason": "CRITICAL -- this is the governance reflection exercise that connects all Day 3 work to responsible AI practices. The discussion it generates is as valuable as the code. Do NOT skip.",
    },
    ("Day3-RAG-Deployment-Capstone/Session4-Debrief-Governance/instructor/Session4_Instructor_Debrief_Governance.ipynb", "Task 4"): {
        "conducting": (
            "Give students 10-12 minutes. This is the final exercise of the entire 3-day program. "
            "Frame it as: 'If you had to present this system to a McKinsey partner for approval to deploy on a client engagement, "
            "what would they want to know?' The go/no-go recommendation forces students to be honest about gaps. "
            "After the exercise, have 2-3 students share their go/no-go decision and blocking issues."
        ),
        "mistakes": [
            "Treating this as a checklist exercise instead of a critical assessment -- students should genuinely evaluate readiness",
            "Not distinguishing between required (blocking) and recommended (non-blocking) criteria",
            "Giving a 'GO' recommendation when there are clearly blocking issues -- practice intellectual honesty",
            "Not considering operational readiness (documentation, runbooks, alerts) -- just focusing on technical features",
            "Skipping the governance section -- this is what differentiates enterprise AI from prototype AI",
        ],
        "skippable": True,
        "skip_reason": "CAN SKIP if running behind schedule for closing. However, this is a great capstone reflection. If skipping, pose the go/no-go question verbally and have a brief class discussion instead. The key message: 'Building the AI system is 50% of the work; making it production-ready and governed is the other 50%.'",
    },
}


def format_instructor_block(data):
    """Format the instructor commentary as markdown to append to a task cell."""
    lines = []
    lines.append("")  # blank line separator
    lines.append("> ---")
    lines.append("> **INSTRUCTOR GUIDANCE**")
    lines.append(">")

    # 1. Conducting the exercise
    lines.append(f"> **How to Conduct This Exercise:** {data['conducting']}")
    lines.append(">")

    # 2. Common mistakes
    lines.append("> **Common Student Mistakes:**")
    for m in data["mistakes"]:
        lines.append(f"> - {m}")
    lines.append(">")

    # 3. Skippable
    if data["skippable"]:
        lines.append(f"> **Skippable?** YES -- {data['skip_reason']}")
    else:
        lines.append(f"> **Skippable?** NO -- {data['skip_reason']}")

    return "\n".join(lines)


def find_task_cell(cells, task_identifier):
    """Find the markdown cell whose HEADING contains the task identifier."""
    import re
    for cell in cells:
        if cell.get("cell_type") != "markdown":
            continue
        source = "".join(cell.get("source", []))
        # Match heading lines like "### Task 1:" or "## Milestone 2:"
        # The task identifier must appear in a markdown heading line (starts with #)
        for line in source.split("\n"):
            stripped = line.strip()
            if stripped.startswith("#") and task_identifier + ":" in stripped:
                return cell
            if stripped.startswith("#") and task_identifier + " " in stripped:
                return cell
    return None


def process_notebook(notebook_path, task_comments):
    """Add instructor commentary to task cells in a notebook."""
    with open(notebook_path, "r") as f:
        nb = json.load(f)

    cells = nb.get("cells", [])
    modified = 0

    for task_id, comment_data in task_comments.items():
        cell = find_task_cell(cells, task_id)
        if cell is None:
            print(f"  WARNING: Could not find '{task_id}' in {os.path.basename(notebook_path)}")
            continue

        # Check if already has instructor guidance
        source_text = "".join(cell.get("source", []))
        if "INSTRUCTOR GUIDANCE" in source_text:
            print(f"  SKIP (already has guidance): {task_id}")
            continue

        # Append instructor commentary
        block = format_instructor_block(comment_data)
        if isinstance(cell["source"], list):
            cell["source"].append(block)
        else:
            cell["source"] += block
        modified += 1
        print(f"  ADDED: {task_id}")

    if modified > 0:
        with open(notebook_path, "w") as f:
            json.dump(nb, f, indent=1)
        print(f"  -> Saved {modified} modifications to {os.path.basename(notebook_path)}")
    else:
        print(f"  -> No modifications needed for {os.path.basename(notebook_path)}")

    return modified


def main():
    # Group comments by notebook
    notebooks = {}
    for (path_suffix, task_id), data in COMMENTS.items():
        full_path = os.path.join(BASE, path_suffix)
        if full_path not in notebooks:
            notebooks[full_path] = {}
        notebooks[full_path][task_id] = data

    total_modified = 0
    for notebook_path, task_comments in sorted(notebooks.items()):
        print(f"\nProcessing: {os.path.relpath(notebook_path, BASE)}")
        if not os.path.exists(notebook_path):
            print(f"  ERROR: File not found!")
            continue
        total_modified += process_notebook(notebook_path, task_comments)

    print(f"\n{'='*60}")
    print(f"DONE: Added instructor commentary to {total_modified} task cells across {len(notebooks)} notebooks.")


if __name__ == "__main__":
    main()
