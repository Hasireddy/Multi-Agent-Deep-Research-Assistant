from typing import Literal
from langgraph.graph import StateGraph, START, END
from agents.state import MessagesState

def should_continue(state: MessagesState)-> str:
    """decides if we should continue the loop or stop based upon whether the
    LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    # If LLM makes a tool call, then perform action
    if last_message.tool_calls:
        return "tool_node"

    # Otherwise , stop and reply to the user
    return END



