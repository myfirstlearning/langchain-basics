import os
from langchain_google_genai import ChatGoogleGenerativeAI

# os.getenv("GOOGLE_API_KEY")

# Set your Google API key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro",
                             google_api_key=GEMINI_API_KEY)

question = input("Enter your question: ")
response = llm.invoke(question)

print(response.content)
