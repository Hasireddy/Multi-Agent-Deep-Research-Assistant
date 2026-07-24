from enum import Enum
from typing import TypedDict

from schemas.planner_schema import SubQuestion
from schemas.searcher_schema import SearchResultSchema


class ResearchStage(str, Enum):
    """
    The pipeline current stage (states of our state machine).
    """
    PLANNING = "planning"
    SEARCHING = "searching"
    VERIFYING = "verifying"
    WRITING = "writing"
    CITING = "citing"
    PRESENTING = "presenting"
    COMPLETED = "completed"
    FAILED = "failed"


# The pipeline needs one state that every node shares so that the whole research is visible.
# We are aware that what was the original query, which stage we are currently in, list of errors happened if any
# and the list of sub-questions we are reasearching on?
class ResearchState(TypedDict, total=False):
    """
    The one shared object passed between nodes
    """
    # Input
    query: str

    stage: ResearchStage
    errors: list[str]

    # Per node output
    sub_questions: list[SubQuestion]
    search_results: list[SearchResultSchema]
    report_generation: str
    create_presentation: str





from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator


class MessagesState(TypedDict):
    """The graph's state is used to store the messages
    and the number of LLM calls."""

    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int