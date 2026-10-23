import os
import requests
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

# weather_api_url = f"https://wttr.in/{city}?format=%C+%t"

def get_weather(city: str):
    response = requests.get(f"https://wttr.in/{city.lower()}?format=%C+%t")
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Could not retrieve weather information."

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