from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="Movie Analyzer", page_icon="🎬", layout="centered")

st.title("🎬 Movie Analysis & Summarizer")

# Pydantic Model
class Movies(BaseModel):
    title: str
    release_year: Optional[int] = None
    rating: Optional[float] = None
    genre: List[str]
    cast: List[str]
    director: Optional[str] = None
    summary: List[str]

parser = PydanticOutputParser(pydantic_object=Movies)

# Text Input
para = st.text_area("Unstructured Movie Paragraph", height=150, placeholder="Type or paste information about a movie...")

if st.button("Analyze Movie", type="primary"):
    if not para.strip():
        st.warning("Please provide a paragraph to analyze.")
    else:
        with st.spinner("Analyzing text..."):
            try:
                model = ChatOpenAI(model="gpt-5-nano")

                prompt = ChatPromptTemplate.from_messages([
                    ("system", """You are a movie analysis and summarization assistant. 
                    Your task is to analyze the movie paragraph provided by the user and create
                    a concise, structured summary in these instructions {format_instructions}."""),
                    ("human", "{paragraph}")
                ])

                final_prompt = prompt.invoke({
                    "paragraph": para,
                    "format_instructions": parser.get_format_instructions()
                })

                # Direct model call followed by parser
                response = model.invoke(final_prompt)
                parsed_output: Movies = parser.parse(response.content)

                st.subheader("JSON Output")
                
                # Render formatted JSON in UI
                st.json(parsed_output.model_dump())
                
                # Code block for easy copying
                st.code(parsed_output.model_dump_json(indent=2), language="json")

            except Exception as e:
                st.error(f"An error occurred: {e}")