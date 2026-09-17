from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableSequence,
    RunnablePassthrough,
    RunnableBranch,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)


parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Write a detailed report on topic: {topic}",
    input_variables=["topic"]
)


prompt2 = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"]
)


report_gen_chain = RunnableSequence(prompt1,model,parser)


summarize_chain = RunnableSequence(RunnableLambda(lambda x: {"text": x}),prompt2,model,parser)


branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500 , summarize_chain),
    RunnablePassthrough()
)


final_chain = RunnableSequence(report_gen_chain,branch_chain)


result = final_chain.invoke({"topic": "AI"})

print(result)