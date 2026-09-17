from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence , RunnableParallel 
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent /".env"  

load_dotenv(env_path)

model  =  ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

prompt1 = PromptTemplate(
    template="Generate a tweet on topic : {topic}" , 
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a linkendIn post for the topic : {topic}",
    input_variables=['topic']
)

parser= StrOutputParser() ; 

parallel_chain = RunnableParallel(
    {
        'tweet' : RunnableSequence(prompt1 , model , parser) , 
        'LinkedIn' : RunnableSequence(prompt2 , model , parser)
    }
)

result  = parallel_chain.invoke({'topic':'AI'}) 

print(result)   # this would return the result in dictionary format 

print(result['tweet']) 

print(result['LinkedIn'])