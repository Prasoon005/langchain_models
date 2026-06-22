from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional, Literal
from pathlib import Path

env_path = Path(__file__).resolve.parent.parent / ".env" 

load_dotenv(env_path)

model  = ChatOpenAI()

#Schema 

class Review(TypedDict):
    key_themes:Annotated[list[str] , "Write down all the key themes discussed in the review in a list"]
    summary:Annotated[str , "Write down the brief summary of the review"]
    sentiment:Annotated[Literal["pos" , "neg"] , "Return the sentiment of the review either negative , positive , neutral"]
    pros:Annotated[Optional[list[str]] , "Write all the pros inside a list"]
    cons:Annotated[Optional[list[str]], "Write all the cons inside a list"]
    name:Annotated[Optional[str],"Write the name of reviewer"]
    
    #Annotated ----> type hinting ---> so that llm easily understands what type of response user is expecting 
    
structured_model  =  model.with_structured_output(Review)


result  = structured_model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.""")

print(result)

print(result['summary'])
print(result['sentiment'])

