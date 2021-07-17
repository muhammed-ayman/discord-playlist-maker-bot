import os
import discord
from Utils import *

# LOAD ENV VARIABLES
TOKEN = os.getenv('DISCORD_TOKEN')

# INITIATE THE UTILS CLASS
utils = Utils()

# DISCORD CLIENT
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} connected successfully')

@client.event
async def on_message(msg):
    utils.pattern_search(msg.content)

client.run(TOKEN)
