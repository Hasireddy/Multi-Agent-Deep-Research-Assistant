import sys
from pathlib import Path

ROOT_PROJECT = Path(__file__).resolve().parents[1]
if str(ROOT_PROJECT) not in sys.path:
    sys.path.insert(0, str(ROOT_PROJECT))


from agents.graph import build_research_graph
from agents.state import ResearchStage


# Visualize graph
#print(agent.get_graph().draw_ascii())

#graph = agent.get_graph()
#png = graph.draw_mermaid_png()

#with open("agent_graph.png", "wb") as f:
    #f.write(png)
#print("Graph saved as agent_graph.png")


def run_agent(query: str):
    graph = build_research_graph()
    return graph.invoke(
        {
            "query": query,
            "stage": ResearchStage.PLANNING
        }
    )


if __name__ == "__main__":
    query = input("Enter your research query: ")
    result = run_agent(query)
    print(f"Stage: {result.get('stage')}")
    for sq in result.get("sub_questions", []):
        print(f"    [{sq.id}]: {sq.question} - {sq.rationale}")

    for sr in result.get("search_results", []):
        print(f"\nSubQuestion ID: {sr.subquestion_id}")
        print(f"Title: {sr.title}")
        print(f"URL: {sr.url}")
        print(f"Content: {sr.content}")
        print("-" * 80)

    print("\n" + "=" * 80)
    print("FINAL REPORT")
    print("=" * 80)

    print("**************************")
    print("\nAvailable keys:")
    print(result.keys())
    print("**************************")

    if result.get("report_generation"):
        print(result["report_generation"])

    print("CREATED PRESENTATION")
    if result.get("create_presentation"):
        print(result["create_presentation"])


    for error in result.get("errors", []):
        print(f"ERROR: {error}")



