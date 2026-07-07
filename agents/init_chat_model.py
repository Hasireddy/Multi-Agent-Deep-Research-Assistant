import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")

model = init_chat_model("gpt-4o-mini", api_key=api_key, temperature=0,max_tokens=200)

response = model.invoke("Why do parrots talk?")
print(response)