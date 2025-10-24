import os
from langchain_openai import ChatOpenAI

## Make sure to set your OpenAI API key in the environment variable
OPEN_API_KEY = os.getenv('OPENAI_API_KEY')
llm=ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

question = input("Enter your question: ")
## Invoke the LLM
response = llm.invoke(question)

## Print the response
print(response.content)


