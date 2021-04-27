'''
discord bot webscraper for CS:GO stats
Logan Lupeamanu
https://github.com/LoganLupe3/discord-bot-webscraper
'''

import requests
import json
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

description = '''Discord CS:GO stat bot that fetches the user's CS:GO stats via webscraping.


Various commands included.'''

bot = commands.Bot(command_prefix='?', description=description)

f = open("../constants/token.json")
data = json.load(f)
TOKEN = data["token"]


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers"""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined in {member.joined_at}')


bot.run(TOKEN)