from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
from pathlib import Path
from pydantic import BaseModel , Field
from typing import Optional , Literal

env_path = Path(__file__).resolve.parent.parent /".env"

load_dotenv(env_path) 

model = ChatOpenAI()

json_format = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "Write down the brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": [
        "positive",
        "negative",
        "neutral"
      ],
      "description": "Return the sentiment of the review either negative, positive, neutral"
    },
    "pros": {
      "type":["array" ,"null"],
      "item":{
          "type":"string"
      },
      "description": "Write all the pros inside a list"
    },
    "cons": {
      "type":["array" ,"null"],
      "item":{
          "type":"string"
      },
      "description": "Write all the cons inside a list"
    },
    "name": {
      "type":["string" , "null"],
      "description": "Write the name of reviewer"
    }
  },
  "required": [
    "key_themes",
    "summary",
    "sentiment"
  ]
}

structured_model = model.with_structured_output(json_format)

result  = structured_model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.""")

print(result)

