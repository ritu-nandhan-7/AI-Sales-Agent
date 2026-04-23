from typing import TypedDict
from langgraph.graph import StateGraph, END

from intent_detector import detect_intent
from rag_engine import get_answer


# State structure
class AgentState(TypedDict):
    user_input: str
    intent: str
    response: str


# Step 1 → Detect intent
def detect_intent_node(state):
    user_input = state["user_input"]
    intent = detect_intent(user_input)

    return {
        "user_input": user_input,
        "intent": intent,
        "response": ""
    }


# Step 2 → Greeting response
def greeting_node(state):
    return {
        **state,
        "response": "Hello! Welcome to AutoStream 😊"
    }


# Step 3 → Inquiry response (RAG)
def inquiry_node(state):
    answer = get_answer(state["user_input"])

    return {
        **state,
        "response": answer
    }


# Step 4 → High-intent response
def high_intent_node(state):
    return {
        **state,
        "response": "Great! Let's get your details for signup."
    }


# Routing logic
def route_intent(state):
    return state["intent"]


# Build graph
builder = StateGraph(AgentState)

builder.add_node("detect_intent", detect_intent_node)
builder.add_node("greeting", greeting_node)
builder.add_node("inquiry", inquiry_node)
builder.add_node("high_intent", high_intent_node)

builder.set_entry_point("detect_intent")

builder.add_conditional_edges(
    "detect_intent",
    route_intent,
    {
        "greeting": "greeting",
        "inquiry": "inquiry",
        "high_intent": "high_intent"
    }
)

builder.add_edge("greeting", END)
builder.add_edge("inquiry", END)
builder.add_edge("high_intent", END)

graph = builder.compile()