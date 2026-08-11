from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

class Movies(BaseModel):
    title: str = Field(description="Title of the movie")
    release_year: Optional[int] = Field(default=None, description="Release year")
    rating: Optional[float] = Field(default=None, description="Rating of the movie")
    genre: List[str] = Field(default_factory=list, description="List of genres")
    cast: List[str] = Field(default_factory=list, description="Main cast members")
    director: str = Field(description="Director name")
    summary: List[str] = Field(default_factory=list, description="Summary points")

parser = PydanticOutputParser(pydantic_object=Movies)

para = input("Give me your unstructured para of movies: ")

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

output = model.invoke(final_prompt)

print(output.content)