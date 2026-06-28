from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path
from langchain_core.prompts import PromptTemplate

env_path =  Path(__file__).resolve.parent.parent /".env"

load_dotenv(env_path)

model = ChatOpenAI()

parser = StrOutputParser() 

template_1  = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=["topic"]
)

template_2 = PromptTemplate(
    template="Provide me  5 line summary on the following text {text}",
    input_variables=["text"]
)

chain = template_1 | model | parser | template_2 | model | parser

result  = chain.invoke({"topic":"BlackHole"})

print(result)

