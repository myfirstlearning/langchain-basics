import os

from langchain_openai import ChatOpenAI
from langchain_core.globals import set_debug
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Enable debug mode to see the full traceback
set_debug(True)

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")  # Ensure the OpenAI API key is set in your environment
llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

# This prompt is used to generate the title for the speech
title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are an experienced speech writer.
    You need to craft an impactful title for a speech on the following topic: {topic}
    Answer exactly with one title.
    """
)

# This prompt is used to generate the speech
speech_prompt = PromptTemplate(
    input_variables=["title"],
    template="""You need to write a powerful speech of 350 words on the following title: {title}
    """
)

# LCEL -> Language Chain Expression Language
# pipe operator (|) to create the chain with prompt_template | llm,
# which is part of LangChain Expression Language (LCEL)
# StrOutputParser() is used to parse the output of the LLM from first_chain
# lambda function is used to extract the title from the response object returned by the StrOutputParser and assign it to the variable title
# st.write is used to display the title in the Streamlit app
# [1] selects the second element of the tuple (the title string)
first_chain = title_prompt | llm | StrOutputParser() | (lambda title: (st.write(title), title)[1])
second_chain = speech_prompt | llm

# The final chain is the result of the first chain piped into the second chain
final_chain = first_chain | second_chain


st.title("Speech Generator")

topic = st.text_input("Enter the topic: ")


if topic:
    with st.spinner(f"Generating speech on {topic}..."):
         response = final_chain.invoke({ "topic":topic})
    st.write(response.content)