from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve.parent.parent / ".env"
load_dotenv(env_path)

model = ChatOpenAI()

messages = [SystemMessage(content="You are helpful ai assistant"),
            HumanMessage(content="Tell me about Langchain")
]

result  =  model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
