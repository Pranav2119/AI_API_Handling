import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set. Add it to a local .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

System_Prompt = """You are a helpful assistant. And only answer the question that is asked. Do not provide any additional information or context.
"""

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {   "role": "system",
            "content": System_Prompt
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message.content)