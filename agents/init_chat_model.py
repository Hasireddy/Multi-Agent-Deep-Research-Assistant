import os
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

from tools.web_research_tool import researcher

load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")

model = init_chat_model("gpt-4o-mini", api_key=api_key, temperature=0,max_tokens=200, timeout=60, max_retries=6)

# Augment LLM with tools
tools = [researcher]
tools_by_name = {tool.name: tool for tool in tools}
print(tools_by_name)

# Bind available tools to the model so it can decide when and how to call them.
model_with_tools = model.bind_tools(tools)

response = model_with_tools.invoke("Explain differences between lithium and Iron batteries?")
print(response.content_blocks)