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
        p = random.choice(list(pokemon.keys()))
        print(p)
        pname = pokemon.get(p)
        await client.send_file(client.get_channel('512765323116806158'), 'pokemon/' + p)
        timeout_end = time.time() + 10
        while time.time() < timeout_end:
            answer = await client.wait_for_message(channel=client.get_channel('512765323116806158'))
            print(answer.content)
            if answer.content != '':
                break
        if answer.content == pname:
            await client.send_message(client.get_channel('512765323116806158'), 'correct, good job!')
            
        elif answer.content != pname:
            await client.send_message(client.get_channel('512765323116806158'), 'incorrect')
        
        await client.send_message(message.channel, 'done')
        

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
