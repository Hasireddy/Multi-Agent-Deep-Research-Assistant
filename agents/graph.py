from langgraph.graph import StateGraph, START, END
from agents.state import MessagesState
from  agents.nodes.llm_node import llm_call
from  agents.nodes.tool_node import tool_node
from  agents.nodes.conditional_edge import should_continue


# Builds the Graph(workflow)
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    ["tool_node", END]
)
agent_builder.add_edge("tool_node", "llm_call")

#Compile the agent
agent = agent_builder.compile()





