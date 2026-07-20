from langgraph.graph import StateGraph, START, END

from agents.research_nodes.planner_node import make_planner_node, make_openai_plan_function, PlanFunction
from agents.state import ResearchState

def build_research_graph(plan_fn: PlanFunction | None = None):
    """
    Build and compile the pipeline graph to be called.
    """
    if plan_fn is None:
        plan_fn = make_openai_plan_function()
    agent_builder = StateGraph(ResearchState)
    agent_builder.add_node("planner", make_planner_node(plan_fn))
    agent_builder.add_edge(START, "planner")
    agent_builder.add_edge("planner", END)

    return agent_builder.compile()


