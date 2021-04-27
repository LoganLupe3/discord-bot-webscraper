'''
discord bot webscraper for CS:GO stats
Logan Lupeamanu
https://github.com/LoganLupe3/discord-bot-webscraper
'''

import requests
import json
from bs4 import BeautifulSoup
import discord

f = open("../constants/token.json")
data = json.load(f)
TOKEN = data["token"]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)