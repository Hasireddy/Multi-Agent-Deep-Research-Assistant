from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator


class MessagesState(TypedDict):
    """The graph's state is used to store the messages
    and the number of LLM calls."""

    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int