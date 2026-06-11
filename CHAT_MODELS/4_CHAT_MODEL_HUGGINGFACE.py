from dotenv import load_dotenv
from pathlib import Path
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os


env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("What is the capital of India?")
print(result.content)