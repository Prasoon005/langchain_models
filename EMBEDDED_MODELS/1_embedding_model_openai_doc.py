from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

embedding_model  =  OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimension = 32
)

document = [
    "delhi is the capital of India ",
    "Paris is the capital of France",
    "New York is the capital of America"
]

result = embedding_model.embed_documents(document)

print(str(result))