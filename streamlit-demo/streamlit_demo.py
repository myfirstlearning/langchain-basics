import os
from langchain_openai import ChatOpenAI
from langchain_core.globals import set_debug
import streamlit as st


# Enable debug mode to see the full traceback
set_debug(True)

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")  # Ensure the OpenAI API key is set in your environment
llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

st.title("Chat with OpenAI")

question = st.text_input("Enter your question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)



