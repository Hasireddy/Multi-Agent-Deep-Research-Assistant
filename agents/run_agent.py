from agents.graph import agent
from langchain.messages import HumanMessage

# Visualize graph
#print(agent.get_graph().draw_ascii())

#graph = agent.get_graph()
#png = graph.draw_mermaid_png()

#with open("agent_graph.png", "wb") as f:
    #f.write(png)
#print("Graph saved as agent_graph.png")


#Starting point to run the Graph
# langGraph passes the messages and llm_calls from node to node
def run_agent():
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

    return response


if __name__ == "__main__":
    run_agent()

