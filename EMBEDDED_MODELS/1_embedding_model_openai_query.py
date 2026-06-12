from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)

result = embedding.embed_query("Delhi is the capital of India")

print(result)