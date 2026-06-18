from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
import streamlit as st

env_path =  Path(__file__).resolve().parent.parent/".env"
load_dotenv(env_path)

chat_model  = ChatOpenAI(model = 'gpt-4o' , temperature=1.5, max_completion_tokens=10)

st.header('Research Tool')

paper_input  = st.selectbox("Select Research Papername : " , ["Select..." , "Attention Is You all need" , "BERT : Pre training ofbidirectional Transformers", "Gpt3 : Language models are few shot learners","Diffusion model Beat GANs on image synthesis"])
style_input = st.selectbox("Select Explanation style : " , ["Beginner-Friendly" ,"Technical" , "Code-Oriented" , "Mathematical" ])
length_input = st.selectbox("Select Explanation length : ",["Short(1-2 paragraphs)","Medium(3-5 paragraphs)" , "Long(detailed explanation)"])

#template
template = PromptTemplate(
template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets where
applicable.
2. Analogies:
- Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.""" ,
input_variables=['paper_input' , 'style_input' , 'length_input'],
validate_template=True
)


#fill the placeholders


if st.button("Summarize"):
    prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    })

    result  = chat_model.invoke(prompt)
    st.write(result.content)


