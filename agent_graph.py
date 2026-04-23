from typing import TypedDict
from tools import mock_lead_capture
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
    # First show Pro Plan details
    answer = get_answer("pro plan")
    print("Agent:", answer)

    print("\nAgent: Great! I'd love to help you get started.")

    name = input("Agent: Please tell me your name: ")
    email = input("Agent: Please enter your email: ")
    platform = input("Agent: Which creator platform do you use? (YouTube/Instagram/etc): ")

    # Tool execution
    mock_lead_capture(name, email, platform)

    return {
        **state,
        "response": "Our team will contact you soon 🚀"
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