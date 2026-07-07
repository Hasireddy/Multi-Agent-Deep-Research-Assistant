from langchain.tools import tool


@tool
def researcher(topic: str)-> str:
    """This tool researches a topic and provides
    response."""
    return f"Researching: {topic}"

