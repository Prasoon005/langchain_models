from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st

env_path =  Path(__file__).resolve().parent.parent/".env"
load_dotenv(env_path)

chat_model  = ChatOpenAI(model = 'gpt-4o' , temperature=1.5, max_completion_tokens=10)

st.header('Research Tool')

paper_input  = st.selectbox("Select Research Papername : " , ["Select..." , "Attention Is You all need" , "BERT : Pre training ofbidirectional Transformers", "Gpt3 : Language models are few shot learners","Diffusion model Beat GANs on image synthesis"])
style_input = st.selectbox("Select Explanation style : " , ["Beginner-Friendly" ,"Technical" , "Code-Oriented" , "Mathematical" ])
length_input = st.selectbox("Select Explanation length : ",["Short(1-2 paragraphs)","Medium(3-5 paragraphs)" , "Long(detailed explanation)"])

template = load_prompt('template.json')

#fill the placeholders


if st.button("Summarize"):
    prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    })

    result  = chat_model.invoke(prompt)
    st.write(result.content)


