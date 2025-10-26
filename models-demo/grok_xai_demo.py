import os
from langchain_xai import ChatXAI

# Initialize the model
llm = ChatXAI(
    model="grok-beta",
    api_key=os.getenv("GROK_API_KEY")  # or GROK_API_KEY
)

response = llm.invoke("Explain LLM in simple terms")
print(response.content)