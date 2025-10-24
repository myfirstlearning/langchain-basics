import os

# from langchain_community.chat_models import ChatOllama -- Deprecated
from langchain_ollama import ChatOllama


## When using Ollama with the Gemma model, no API key is required.
## ChatOllama from langchain_community uses the local Ollama instance;
## just ensure Ollama is installed and running.
## os.getenv("GEMMA_API_KEY")  # not needed for local Ollama
##os.getenv("GEMMA_API_KEY")

llm = ChatOllama(model="gemma:2b")

question = input("Enter your question: ")
response = llm.invoke(question)

print(response.content)