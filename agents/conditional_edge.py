from typing import Literal
from langgraph.graph import StateGraph, START, END
from state import MessagesState

def should_continue(state: MessagesState)-> Literal["tool_node", END]:
    """decides if we should continue the loop or stop based upon whether the
    LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    # If LLM makes a tool calal, then perform action
    if last_message.tool_calls:
        return "tool_node"

    # Otherwise , stop and reply to the user
    return END



