import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")

def init_model():
    model = init_chat_model(
        "gpt-4o-mini",
                api_key=api_key,
                temperature=0,
                max_tokens=1000,
                timeout=60,
                max_retries=6
        )
    return model
