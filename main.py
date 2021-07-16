import os
import discord
from dotenv import load_dotenv
import utils

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} connected successfully')

@client.event
async def on_message(msg):
    utils.search(msg.content)

client.run(TOKEN)
