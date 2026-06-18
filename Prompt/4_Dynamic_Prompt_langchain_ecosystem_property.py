from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.prompts import load_prompt
import streamlit as st

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

chat_model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,
    max_completion_tokens=1000
)

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name:",
    [
        "Select...",
        "Attention Is All You Need",
        "BERT: Pre-training of Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style:",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length:",
    ["Short", "Medium", "Long"]
)

template = load_prompt("template.json")

if st.button("Summarize"):

    chain = template | chat_model

    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(result.content)