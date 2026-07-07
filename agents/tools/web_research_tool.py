from langchain.tools import tool

def create_researcher_tool(llm):
    @tool
    def researcher(topic: str)-> str:
        """This tool researches a topic and provides
        response."""

        prompt = f"""
                You are a helpful research assistant.
                Your task is to search for a topic provided by the user and
                generate three to five sub queries related to the topic.
                Do not assume or add external knowledge.
                Explain the rationale behind your answer. 
                Include:
                - key factors considered
                - assumptions made
                - evidence or examples supporting the conclusion
                - possible alternatives
                
                Topic: {topic}
        """
        response = llm.invoke(prompt)
        return response.content
    return researcher



