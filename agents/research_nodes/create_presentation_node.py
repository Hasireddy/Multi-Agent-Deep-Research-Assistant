from agents.config import init_model
from agents.prompts import PRESENTATION_PROMPT
from agents.state import ResearchState, ResearchStage


def create_presentation(report):
    """Creates a presentation from the final generated report"""
    llm = init_model()
    response = llm.invoke([
        ("system", PRESENTATION_PROMPT),
        ("human", report)
    ])
    content = response.content if hasattr(response, "content") else str(response)

    return content.replace("\\n", "\n")


def presentation_node(state: ResearchState):
    #print("Entered Presentation Node")
    report_generation = state["report_generation"]

    if not report_generation:
        return {
            "stage": ResearchStage.FAILED,
            "errors": ["No search results found."]
        }

    try:
        presentation = create_presentation(report_generation)
        return {
            "create_presentation": presentation,  # or report if your model returns a string
            "stage": ResearchStage.COMPLETED
        }

    except Exception as e:
        return {
            "stage": ResearchStage.FAILED,
            "errors": [f"Report generation failed: {e}"]
        }