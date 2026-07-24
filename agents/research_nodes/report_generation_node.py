from agents.config import init_model
from agents.prompts import REPORT_GENERATION_PROMPT
from agents.state import ResearchState, ResearchStage
from schemas.searcher_schema import SearchResultSchema

def report_generation(search_results: list[SearchResultSchema]):
    """Generates final report from the searched results"""
    llm = init_model()

    context = "\n\n".join(
        f"""
    Subquestion ID: {result.subquestion_id}
    Title: {result.title}
    URL: {result.url}
    Content:
    {result.content}
    """
     for result in search_results
    )

    response = llm.invoke([
        ("system", REPORT_GENERATION_PROMPT),
        ("human", context)
    ])
    return response



def report_generation_node(state: ResearchState):
    #print("Entered report_generation_node")
    search_results = state["search_results"]

    if not search_results:
        return {
            "stage": ResearchStage.FAILED,
            "errors": ["No search results found."]
        }

    try:
        report = report_generation(search_results)

        #print(f"REPORT: {report}")
        #print(type(report))

        return {
            "report_generation": report.content,  # or report if your model returns a string
            "stage": ResearchStage.PRESENTING
        }

    except Exception as e:
        return {
            "stage": ResearchStage.FAILED,
            "errors": [f"Report generation failed: {e}"]
        }


