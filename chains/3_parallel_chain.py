from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
from pathlib import Path

import os

env_path = Path(__file__).resolve().parent.parent /".env"

load_dotenv(env_path)

chat_model1 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

chat_model2  = ChatOpenAI(
    model="gpt-4.1",
    temperature=1.5, 
    max_completion_tokens=10,
    api_key=os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 5 question and answer from the following text \n {text}" ,
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template = "Merge the provided noted and quiz into a single document \n notes -> {notes} and quiz -> {quiz}" ,
    input_variables = ['notes', 'quiz']
)


parallel_task = RunnableParallel(
    {
        'notes' : prompt1 | chat_model1 | parser ,
        'quiz' : prompt2 | chat_model2 | parser
    }
)

merge_chain  =  prompt3 | chat_model1 | parser 

chain = parallel_task | merge_chain 

text = """
The Kubernetes API lets you query and manipulate the state of objects in Kubernetes. The core of Kubernetes' control plane is the API server and the HTTP API that it exposes. Users, the different parts of your cluster, and external components all communicate with one another through the API server.
The core of Kubernetes' control plane is the API server. The API server exposes an HTTP API that lets end users, different parts of your cluster, and external components communicate with one another.

The Kubernetes API lets you query and manipulate the state of API objects in Kubernetes (for example: Pods, Namespaces, ConfigMaps, and Events).

Most operations can be performed through the kubectl command-line interface or other command-line tools, such as kubeadm, which in turn use the API. However, you can also access the API directly using REST calls. Kubernetes provides a set of client libraries for those looking to write applications using the Kubernetes API.

Each Kubernetes cluster publishes the specification of the APIs that the cluster serves. There are two mechanisms that Kubernetes uses to publish these API specifications; both are useful to enable automatic interoperability. For example, the kubectl tool fetches and caches the API specification for enabling command-line completion and other features. The two supported mechanisms are as follows
"""

result  = chain.invoke({'text':text})

print(result)


