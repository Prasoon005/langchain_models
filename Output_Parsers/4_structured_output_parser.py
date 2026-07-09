from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StructuredOutputParser,
    ResponseSchema,
)
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

Chat_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

schema = [
    ResponseSchema(name="fact_1", description="Fact about the topic"),
    ResponseSchema(name="fact_2", description="Fact about the topic"),
    ResponseSchema(name="fact_3", description="Fact about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

Prompt = PromptTemplate(
    template="Give 3 facts about {topic}\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    },
)

chain = Prompt | Chat_model | parser

result = chain.invoke({"topic": "blackhole"})

print(result)