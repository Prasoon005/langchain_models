from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
import os 

env_path  = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)

model  = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

prompt1 = PromptTemplate(
    template="Tell me a joke about a topic : {text}" , 
    input_variables=['text']
)

parser  = StrOutputParser() 

prompt2  = PromptTemplate(
    template="explain the joke mentioned here : {joke}" , 
    input_variables=['joke']
)

chain = RunnableSequence(prompt1 , model , parser , prompt2 , model , parser)
result  = chain.invoke({'text' : 'AI'})
print(result) 

