from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from pathlib import Path
from langchain_core.prompts import PromptTemplate

env_path =  Path(__file__).resolve().parent.parent /".env"

load_dotenv(env_path)

model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
  template="Give a name  ,  age  , location of random person {format_description}",
  input_variables=[] ,
  partial_variables={"format_description":parser.get_format_instructions()} 
)

chain = template | model | parser 

result  = chain.invoke({})

print(result)
print(type(result))    #<class 'dict'>