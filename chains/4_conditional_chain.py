from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal
from langchain_core.runnables import RunnableBranch , RunnableLambda
from dotenv import load_dotenv
from pathlib import Path

import os

env_path = Path(__file__).resolve().parent.parent /".env"

load_dotenv(env_path)

chat_model1 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

class feedback_format(BaseModel):
    sentiment : Literal['positive' , 'negative'] = Field(description="Provide the sentiment of the given feedback")


parser1  = PydanticOutputParser(pydantic_object=feedback_format)

prompt1 = PromptTemplate(
    template="Generate a sentiment either positive or negative from given feedback -> {feedback} \n {format_instruction}",
    input_variables = ['feedback'] ,
    partial_variables= {'format_instruction':parser1.get_format_instructions()}
)

classifier_chain = prompt1 | chat_model1 | parser1

feedback = "This phone is worst in charging and its battery drain fastly"

prompt2 = PromptTemplate(
    template='Generate a appropriate response  to this positive feedback \n {positive_feedback}' ,
    input_variables=['positive_feedback']
)

prompt3 = PromptTemplate(
    template='Generate a appropriate response  to this negative feedback \n {negative_feedback}' ,
    input_variables=['negative_feedback']
)

parser2 = StrOutputParser()

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive' , RunnableLambda(lambda x : {'positive_feedback':feedback})| prompt2 | chat_model1 | parser2),
    (lambda x:x.sentiment == 'negative' ,RunnableLambda(lambda x : {'negative_feedback':feedback}) | prompt3 | chat_model1 | parser2),
    RunnableLambda(lambda x :"User doesnot provide any sentiment")
)

chain = classifier_chain | branch_chain 

result  = chain.invoke({'feedback': feedback})

print(result) 




