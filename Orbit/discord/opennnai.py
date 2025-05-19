import openai
import os
from dotenv import load_dotenv

print("Debug: Starting to load environment...")
load_dotenv()

print(f"Debug: GPTKEY present: {'Yes' if os.getenv('GPTKEY') else 'No'}")
openai.api_key = os.getenv('GPTKEY')
print(f"Debug: API key set to OpenAI: {'Yes' if openai.api_key else 'No'}")

def chatgpt_response(content):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": content}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
