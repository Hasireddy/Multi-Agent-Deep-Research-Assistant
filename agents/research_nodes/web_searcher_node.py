import os
from tavily import TavilyClient
from dotenv import load_dotenv
from pprint import pprint

from agents.state import ResearchState, ResearchStage
from schemas.planner_schema import SubQuestion
from schemas.searcher_schema import SearchResultSchema

load_dotenv()
tavily_key = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=tavily_key)



def web_search(sub_question):
    """Searches relevant web results for a sub-query and returns the response"""
    # Each subquery is an object SubQuestion(id=0, question="What are apples?")
    response = tavily_client.search(
        sub_question.question,
        max_results=2
    )
    print("*************************RESPONSE*********")
    print(response.get("results"))
    return [
        SearchResultSchema(
        subquestion_id = sub_question.id,
        url = r.get('url'),
        title = r.get('title'),
        content = r.get('content')[:800]
    )
    for r in response.get("results")

    ]



def searcher_node(state: ResearchState):
    """Loops through all subqueries and return the results"""
    sub_queries = state["sub_questions"]

    if not sub_queries:
        return {
            "stage": ResearchStage.FAILED,
            "errors": ["Searcher: received an empty sub queries."]
        }

    try:
        web_search_results = []
        for subquery in sub_queries:
            result = web_search(subquery)
            web_search_results.extend(result)
        return {
            "search_results": web_search_results,
            "stage": ResearchStage.WRITING
        }

    except Exception as e:
        return {
            "stage": ResearchStage.FAILED,
            "errors": [f"Searcher failed: {e}"]
        }



"""mock_state: ResearchState = {
    "sub_questions": [
        SubQuestion(id=0, question="What are apples?"),
        SubQuestion(id=1, question="What is Python?")
    ]
}

results = searcher_node(mock_state)
pprint(results)"""



