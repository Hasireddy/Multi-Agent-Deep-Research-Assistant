from agents.graph import agent
from langchain.messages import HumanMessage

response = agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="Explain differences between lithium and iron batteries."
            )
        ],
        "llm_calls": 0
    }
)

for message in response["messages"]:
    message.pretty_print()