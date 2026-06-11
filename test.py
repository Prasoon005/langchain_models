from dotenv import load_dotenv
import os

load_dotenv()

print("TOKEN =", os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))