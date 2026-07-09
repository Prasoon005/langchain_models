from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import Field , BaseModel

import os

env_path = Path(__file__).resolve().parent.parent /".env" 

load_dotenv(env_path)

Chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Pydantic object

class Person(BaseModel):
    name : str = Field(description="Name of the person")
    age : int = Field(gt=18 , description="Age of the person")
    city:str = Field(description="city of the person")

parser = PydanticOutputParser(pydantic_object=Person)

prompt = PromptTemplate(
    template="Generate the name , age and city of a fictional {place} person \n {format_instruction}" ,
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain  = prompt | Chat_model | parser

result  = chain.invoke({'place':'indian'})

print(type(result))

