from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
from pathlib import Path
from pydantic import BaseModel , Field
from typing import Optional , Literal

env_path = Path(__file__).resolve.parent.parent /".env"

load_dotenv(env_path) 

model = ChatOpenAI()

class Review(BaseModel):
    key_themes : list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary : str = Field(description="Write down the brief summary of the review")
    sentiment:Literal["positive" , "negative" , "neutral"] = Field(description="Return the sentiment of the review either negative , positive , neutral")
    pros:Optional[list[str]] = Field(default=None ,description= "Write all the pros inside a list")
    cons:Optional[list[str]] = Field(default=None,description="Write all the cons inside a list")
    name:Optional[str] = Field(default=None,description="Write the name of reviewer")

structured_model = model.with_structured_output(Review)

result  = structured_model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.""")

print(result)

