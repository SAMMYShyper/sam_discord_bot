from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("GPTKEY"))

def chatgpt_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "You are a productivity bot. Just be natural and correct"},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=200
        )
        print(response.usage)
        return response.choices[0].message.content.strip()
# c
    except Exception as e:
        return f"Error: {str(e)}"
