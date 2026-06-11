from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model  = ChatOpenAI(model = 'gpt-4' , temperature=1.5, max_completion_tokens=10) #temperature define randomness , creativity 
result = chat_model.invoke("What is the capital of France")
print(result.content)
