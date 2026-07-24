from langgraph.graph import StateGraph, START, END

from agents.research_nodes.planner_node import make_planner_node, make_openai_plan_function, PlanFunction
from agents.research_nodes.web_searcher_node import searcher_node
from agents.research_nodes.report_generation_node import report_generation_node
from agents.research_nodes.create_presentation_node import presentation_node
from agents.state import ResearchState

def build_research_graph(plan_fn: PlanFunction | None = None):
    """
    Build and compile the pipeline graph to be called.
    """
    if plan_fn is None:
        plan_fn = make_openai_plan_function()

    agent_builder = StateGraph(ResearchState)
    agent_builder.add_node("planner", make_planner_node(plan_fn))
    agent_builder.add_node("searcher", searcher_node)
    agent_builder.add_node("generator", report_generation_node)
    agent_builder.add_node("presenter", presentation_node)

    agent_builder.add_edge(START, "planner")
    agent_builder.add_edge("planner", "searcher")
    agent_builder.add_edge("searcher", "generator")
    agent_builder.add_edge("generator", "presenter")
    agent_builder.add_edge("presenter", END)

    return agent_builder.compile()


