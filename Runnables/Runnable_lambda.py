from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough ,RunnableLambda
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

def word_counter(text):
    return len(text.split())


# first create a joke -- joke creation

joke_creation = RunnableSequence(prompt1 , model , parser) 

parallel_chain = RunnableParallel(
    {
        'joke':RunnablePassthrough() , 
        'joke_word_counter': RunnableLambda(word_counter)
    }
)

final_chain  =  RunnableSequence(joke_creation , parallel_chain)

result  = final_chain.invoke({'topic' : 'AI'})

print(result) 

