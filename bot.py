from keep_alive import keep_alive
import discord
import os
import time
from pokemon import pokemon
import random

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith('$wtp'):
        # max_time = 5
        # start_time = time.time()
        # while (time.time() - start_time) < max_time:
        p = pokemon.(pokemon.keys)
        print(pokemon)
        await client.send_file(client.get_channel('512765323116806158'), 'bulbasaur.png')
        await client.wait_for_message(timeout=10, channel=client.get_channel('512765323116806158'), content='bulbasaur')
        await client.send_message(message.channel, 'done')
        

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
