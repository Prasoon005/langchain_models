from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage ,HumanMessage,AIMessage
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,
    max_completion_tokens=1000
)

Chat_history = [SystemMessage(content='You are a helpful Ai assistant ')]


while(True):
    user_input  =  input("User : ")
    Chat_history.append(HumanMessage(content=user_input))
    if(user_input=="exit"):
        break
    result  = model.invoke(user_input)
    Chat_history.append(AIMessage(content=result.content))
    print("Ai : " , result.content)
print(Chat_history)
