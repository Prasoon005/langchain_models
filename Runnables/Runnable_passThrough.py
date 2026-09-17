from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough 
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path

env_path =Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

parser = StrOutputParser() 

prompt1 = PromptTemplate(
    template="Tell me a joke on topic : {topic}" , 
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Give me an explanation of this joke : {joke}" , 
    input_variables=['joke']
)

seq_chain  = RunnableSequence(prompt1 , model , parser)

parallel_chain= RunnableParallel(
    {
        'joke': RunnablePassthrough() , 
        'explanation':RunnableSequence(prompt2 , model , parser)
    }
)

final_chain = RunnableSequence(seq_chain , parallel_chain)

result  = final_chain.invoke({'topic':'AI'})

print(result) 

print(result['joke'])

print(result['explanation'])
