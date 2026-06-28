from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate

env_path = Path(__file__).resolve.parent.parent /".env"

load_dotenv(env_path)

model  = ChatOpenAI() 


template_1  = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=["topic"]
)

prompt1 = template_1.invoke({"topic":"Blackhole"})

response_1 = model.invoke(prompt1)

template_2 = PromptTemplate(
    template="Provide me  5 line summary on the following text {text}",
    input_variables=["text"]
)

prompt2  = template_2.invoke({"text":response_1.content})

response_2 = model.invoke(prompt2)

print(response_2.content)

