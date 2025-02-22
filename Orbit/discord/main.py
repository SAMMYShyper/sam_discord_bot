import discord
import os
from dotenv import load_dotenv
import requests
import json
from opennai.opennnai import chatgpt_response

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
    elif mes.content.startswith('!quote'):
        quote = get_quote()
        await mes.channel.send(quote)
    elif mes.content.startswith('!affirm'):
        affirm = get_affirm()
        await mes.channel.send(affirm)
    command, user_messge =None, None

    for text in ['!ai']:
        if mes.content.startswith(text):
            command=mes.content.split(' ')[0]
            user_message=mes.content.replace(text, '')
            print(command, user_message)

    if command == '!ai':
        bot_response = chatgpt_response(content=user_message)
        await mes.channel.send(f'Answer: {bot_response}')


    #elif mes.content.startswith('!ai'):


#JSON REQUESTS
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





client.run(magickey)