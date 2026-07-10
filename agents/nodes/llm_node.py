from langchain.messages import SystemMessage
from agents.model import model_with_tools
from agents.state import MessagesState


# Brain of LangGraph agent that decides what to do next
def llm_call(state: MessagesState):
    """This node receives the current state and decides
    whether to call a tool or answer the user"""
    return{
        "messages": [
            model_with_tools.invoke(
                [
                    SystemMessage(
                        content="You are a helpful research assistant."
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get('llm_calls',0) + 1,
    }