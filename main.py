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
    if msg.author != client.user:
        utils.pattern_search(msg.content)
        if len(utils.to_send_msgs) > 0:
            await msg.channel.send(utils.to_send_msgs)
            utils.to_send_msgs = []

client.run(TOKEN)
