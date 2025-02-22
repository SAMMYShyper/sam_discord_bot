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
        max_tokens=5
    )
    response_dict = response.get('choice')
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]['content']
    return prompt_response
