from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

Chat_Model  =  ChatAnthropic(model='claude-3-5-sonnet-20241022')
result  = Chat_Model.invoke("What is the capital of America")
print(result.invoke)

