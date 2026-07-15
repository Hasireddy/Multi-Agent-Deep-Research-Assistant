from config import init_model
from agents.research_nodes.planner_node import create_researcher_tool

# Augment LLM with research_nodes
researcher = create_researcher_tool(init_model)

tools = [researcher]
tools_by_name = {tool.name: tool for tool in tools}
print(tools_by_name)

# Bind available research_nodes to the model so it can decide when and how to call them.
model_with_tools = init_model.bind_tools(tools)
