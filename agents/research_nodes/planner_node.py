from langchain.tools import tool
from typing import Callable
from schemas.planner_schema import Subquestion, PlanResponse
from agents.config import init_model
from agents.prompts import PLANNER_SYSTEM_PROMPT

# It accepts query as string and returns a list of subqueries
PlanFunction = Callable[[str],list[Subquestion]]


def make_openai_plan_function():
    llm = init_model()
    structured_llm = llm.with_structured_output(
                                    PlanResponse
                                )
    def plan_function(query):
        response = structured_llm.invoke(
            [
                ("System",PLANNER_SYSTEM_PROMPT),
                ("Human", query)
            ]
        )
        return response.subquestions

    return plan_function



def create_researcher_tool(llm):
    @tool
    def researcher(topic: str)-> str:
        """This tool researches a topic and provides
        response."""

        prompt = {PLANNER_SYSTEM_PROMPT}
        Topic: {topic}

        response = llm.invoke(prompt)
        return response.content
    return researcher



