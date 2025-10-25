import os

from langchain_openai import ChatOpenAI
from langchain_core.globals import set_debug
import streamlit as st
from langchain_core.prompts import PromptTemplate


# Enable debug mode to see the full traceback
set_debug(True)

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")  # Ensure the OpenAI API key is set in your environment
llm = ChatOpenAI(model="gpt-4o", api_key=OPEN_API_KEY)


prompt_template = PromptTemplate(
    input_variables=["country", "no_of_paragraphs", "language"], ##Optional
    template="""You are an expert in traditional cuisines.
    You provide information about a specific dish from a specific country.
    Answer the question: What is a traditional dish from {country}?
    Answer in {no_of_paragraphs} paragraphs in {language}.
    """
)


## Newer LangChain versions
prompt_template_one = PromptTemplate.from_template(
    template="""You are an expert in traditional cuisines.
    You provide information about a specific dish from a specific country.
    Answer the question: What is a traditional dish from {country}?
      Answer in {no_of_paragraphs} paragraphs in {language}.
    """
)

## Simpler way to create PromptTemplate in newer LangChain versions
prompt_template_smp = PromptTemplate(
    template="""You are an expert in traditional cuisines.
    You provide information about a specific dish from a specific country.
    Answer the question: What is a traditional dish from {country}?
    Answer in {no_of_paragraphs} paragraphs in {language}.
    """
)

st.title("Cuisine Info")

country = st.text_input("Enter the country:")
no_of_paragraphs = st.number_input("Number of paragraphs:", min_value=1, max_value=5)
language = st.selectbox("Select language:", ["English", "French", "Spanish", "Hindi", "Chinese", "German"])


if country:
    with st.spinner(f"Finding traditional dishes from {country}..."):
         response = llm.invoke(prompt_template_smp.format(country=country,no_of_paragraphs=no_of_paragraphs,language=language))
    st.write(response.content)



