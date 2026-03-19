import discord
import os
from dotenv import load_dotenv
import requests
import json
from opennai.opennnai import chatgpt_response
from random import choice, randint

load_dotenv()
magickey = os.getenv('SAMSTOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We are in {client.user}')

@client.event
async def on_message(mes):
    if mes.author == client.user:
        return
    if mes.content.startswith('!hi'):
        await mes.reply(f'Hey there {mes.author}!')
    if mes.content.startswith('!help'):
        help_text = f"""
    **Hey there {mes.author}!** 

    Here's what I can do for you right now:

    **Fun Commands:**
    - `!quote` — Get a random quote
    - `!affirm` — Receive a positive affirmation
    - `!flip` — Flip a coin for decisions

    **AI-Powered Command:**
    - `!orbit` — Ask the AI anything (powered by **gpt-4.1-nano**)

    **Notes:**
    - The AI responses may take a few seconds to generate.
    - For feature suggestions or questions, contact @sammyhi
    """
        await mes.reply(help_text)
    elif mes.content.startswith('!flip a coin'):
        await mes.reply(choice(['You flipped heads', 'You flipped tails']))
    elif mes.content.startswith('!quote'):
        quote = get_quote()
        await mes.channel.send(quote)
    elif mes.content.startswith('!affirm'):
        affirm = get_affirm()
        await mes.channel.send(affirm)
    elif mes.content.startswith('!insult'):
        insult = get_insult()
        await mes.channel.send(f'This is for you {mes.author}: {insult}')


    elif mes.content.startswith('!orbit'):
        user_message = mes.content[3:].strip()
        bot_response = chatgpt_response(user_input=user_message)
        await mes.channel.send(f'{bot_response}')

    '''elif mes.content.startswith('!item shop'):
        item_shop = get_item_shop()
        await mes.channel.send(item_shop)
    command, user_message =None, None
'''

'''
    for text in ['!ai']:
        if mes.content.startswith(text):
            command=mes.content.split(' ')[0]
            user_message=mes.content.replace(text, '')
            print(command, user_message)

'''
#JSON REQUESTS
def get_insult():
    response_insult = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    json_data_insult = json.loads(response_insult.text)
    insult = json_data_insult['insult']
    return insult

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote

def get_affirm():
    response_two = requests.get('https://www.affirmations.dev/')
    json_data_two = json.loads(response_two.text)
    affirm = json_data_two['affirmation']
    return affirm

def get_ai():
    pass

'''def get_item_shop():
    response_three = requests.get('https://fortnite-api.com/v2/news')
    json_data_three = json.loads(response_three.text)
    item_shop = json_data_three[['body']
    return item_shop '''

#Baked-In Input and Response
client.run(magickey)