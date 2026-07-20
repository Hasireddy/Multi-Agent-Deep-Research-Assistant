from langchain.tools import tool
from typing import Callable

from agents.state import ResearchState, ResearchStage
from schemas.planner_schema import SubQuestion, PlanResponse
from agents.config import init_model
from agents.prompts import PLANNER_SYSTEM_PROMPT

# It accepts query as string and returns a list of subqueries
PlanFunction = Callable[[str],list[SubQuestion]]


def make_openai_plan_function():
    llm = init_model()
    structured_llm = llm.with_structured_output(
                                    PlanResponse
                                )
    def plan_function(query):
        response = structured_llm.invoke(
            [
                ("system",PLANNER_SYSTEM_PROMPT),
                ("human", query)
            ]
        )
        return response.sub_questions

    return plan_function


# DESIGN PATTERN - Factory Pattern
# LangGraph has a hard rule -> nodes must be a function it should exactly take one argument
# Planner Node requires-> Query (State) & How to Generate a list of Sub Queries (Plan Function)

# We cannot add plan function as second argument so we create it ahead of time using closure.
# Function present inside another function have access to the paremeter accepted by the outer function.

# Dependency Injection Pattern: Tomorrow if the logic of computing the sub questions changes we just need to update the pna function only.


# Difference between node v/s tool?
#------------------------------------------------
# Tools are pre-defined functions or methods provided to LLM to educate them on performing a particular task.
# Howsoever, an LLM may or may not use it depending on the task it might be performing.
# Non-deterministic

# Nodes are unit of execution in a LangGraph workflow. Again this can also be defined as a function or methods.
# But nodes are deterministic in a workflow. An LLM would never skip a Node call in a workflow.
def make_planner_node(plan_fn: PlanFunction) -> Callable[[ResearchState], dict]:
   """
   Node Contract: read state["query"] -> write_state["sub_questions"]
   """
   def planner_node(state: ResearchState) -> dict:
       query = state.get("query") or ""
       if not query:
           return {
            "stage": ResearchStage.FAILED,
            "errors": ["Planner: received an empty query."]
           }

       try:
           sub_questions = plan_fn(query)
       except Exception as exc:
           return {
               "stage": ResearchStage.FAILED,
               "errors": [f"Planner: failed to generate sub-questions with following exception {str(exc)}."]
           }

       if not sub_questions:
           return {
               "stage": ResearchStage.FAILED,
               "errors": [f"Planner: produced empty or no sub questions."]
           }

       # Normalizing ids to clean 0 to n-1 range
       for index, sub_question in enumerate(sub_questions):
           sub_question.id = index

       return {
           "sub_questions": sub_questions,
           "stage": ResearchStage.SEARCHING,
       }

   return planner_node




