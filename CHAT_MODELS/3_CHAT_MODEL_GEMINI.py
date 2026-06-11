from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

Chat_model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
result= Chat_model.invoke("Suggest me some 5 indian names")
print(result.content)