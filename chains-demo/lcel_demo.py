import os

from langchain_openai import ChatOpenAI
from langchain_core.globals import set_debug
import streamlit as st
from langchain_core.prompts import PromptTemplate


# Enable debug mode to see the full traceback
set_debug(True)

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")  # Ensure the OpenAI API key is set in your environment
llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)

## Simpler way to create PromptTemplate in newer LangChain versions
prompt_template = PromptTemplate(
    template="""Welcome o the {city} travel guide!
    If you're visiting in {month}, here's what you can do:
    1. Must-visit attractions:
    2. Local cuisine you must try.
    3. Useful phrases in {language}.
    4. Tips or traveling on a {budget} budget.
    Enjoy your visit!
    """
)

st.title("Cuisine Info")

city = st.text_input("Enter the city:")
month = st.text_input("Enter the month of travel:")
budget = st.selectbox("Travel Budget:", ["Low", "Medium", "High"])
language = st.selectbox("Select language:", ["English", "French", "Spanish", "Hindi", "Chinese", "German"])

# LCEL -> Language Chain Expression Language
# pipe operator (|) to create the chain with prompt_template | llm,
# which is part of LangChain Expression Language (LCEL)
chain = prompt_template | llm

if city and month and budget and language:
    with st.spinner(f"Finding travel plan for {city}..."):
         response = chain.invoke({ "city":city,
                                    "month":month,
                                    "budget":budget,
                                    "language":language
                                    })
    st.write(response.content)