from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pathlib import Path

import os

env_path = Path(__file__).resolve().parent.parent /".env"

load_dotenv(env_path)

chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

parser = StrOutputParser()

template1 = PromptTemplate(
    template="Generate a report on topic {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Generate a short summary of the detailed report :\n\n{report}",
    input_variables=['report']
)

chain  =  template1 | chat_model | parser | template2 | chat_model | parser

final_result  = chain.invoke({'topic':'Van gogh'})

print(final_result)

