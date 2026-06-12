from langchain_huggingface import HuggingFaceEmbeddings #remember here hugging face is in local , no api is used to connect 
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

embedding_model = HuggingFaceEmbeddings(
    model_name= 'sentence-transformers/all-MiniLM-L6-v2'
)

document = [
    "delhi is the capital of India ",
    "Paris is the capital of France",
    "New York is the capital of America"
]

vector = embedding_model.embed_documents(document)

print(str(vector))