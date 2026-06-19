from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

Chat_template = ChatPromptTemplate(
    ('SystemMessage','You are Helpful {domain} expert'),
    ('HumanMessage','Explain in simple terms, what is {topic}')
)

prompt = Chat_template.invoke(
    {
    'domain':'cricket',
    'topic':'Second'
    }
)

print(prompt)

