from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

Chat_Model  =  ChatAnthropic(model='')
result  = Chat_Model.invoke("What is the capital of America")
print(result.invoke)

