from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os 

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = PromptTemplate(
    template="Give a short description about the {topic}" , 
    input_variables=['topic']
)

parser = StrOutputParser()

chain  =  prompt | chat_model | parser

result  = chain.invoke({'topic':'Art'})

print(result)
