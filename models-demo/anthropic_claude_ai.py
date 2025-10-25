import os
from langchain_anthropic import ChatAnthropic


# Set your Google API key
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

# Initialize Claude (make sure to set ANTHROPIC_API_KEY environment variable)
llm = ChatAnthropic(model="claude-sonnet-4-5", api_key=CLAUDE_API_KEY)

question = input("Enter your question: ")
response = llm.invoke(question)

print(response.content)