'''
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('GPTKEY')

def chatgpt_response(content):
    response = openai.Completion.create(
        model='gpt-4o-mini',
        content=content,
        temperature=0.7,
        max_tokens=50
    )
    response_dict = response.get('choice')
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]['content']
    return prompt_response

def chatgpt_response(content):
'''

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

    except Exception as e:
        return f"Error: {str(e)}"
