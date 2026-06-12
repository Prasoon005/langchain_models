from langchain_openai import ChatOpenAI
import streamlit as st 
from dotenv import load_dotenv
from pathlib import Path

env_path =  Path(__file__).resolve().parent.parent/".env"

load_dotenv(env_path)

model = chat_model  = ChatOpenAI(model = 'gpt-4' , temperature=1.5, max_completion_tokens=10)

st.header('Research Tool')

user_input = st.text_input("Enter Your Prompt")

if(st.button('Summarize')):
    result  =  model.invoke(user_input)
    st.write(result.content)