from langchain_core.messages import SystemMessage , HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

Chat_template = ChatPromptTemplate(
    ('system' , 'You are Helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history')
    ('human' , '{query}')
)

chat_history = []

# load chat history
with open('Chat_history.txt') as f:
    chat_history.append(f.readlines())

print(chat_history)

prompt = Chat_template.invoke(
    {
    'query':'Where is my refund' ,
    'chat_history':'chat_history'}
)

print(prompt)