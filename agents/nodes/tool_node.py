from langchain.messages import ToolMessage
from agents.model import tools_by_name

#Calls python function that LLM wants to call as tool
def tool_node(state: dict):
    """Performs tool call and returns ToolMessages"""

    result = []

    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        print("Tool called",tool)
        observation = tool.invoke(tool_call["args"])
        print("Invoked tool call Args", observation)
        result.append(
            ToolMessage(
                content=observation,
                tool_call_id=tool_call["id"],
            )
        )
        print("Result of the called tool", result)

    return {"messages": result}

