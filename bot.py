from keep_alive import keep_alive
from discord.ext import commands
import discord
import os
import time
from pokemon import pokemon
import random

client = discord.Client()
client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith('$wtp'):
        async def get_question():
            p = random.choice(list(pokemon.keys()))
            print(p)
            pname = pokemon.get(p)
            print(pname)
            await client.send_file(client.get_channel('512765323116806158'), 'pokemon/' + p)
            answer = await client.wait_for_message(author=message.author,
                                                    channel=client.get_channel('512765323116806158'),
                                                    timeout=10)
            if answer:
                print(answer.content)  

                if answer.content == pname:
                    time.sleep(0.5)
                    await client.send_message(client.get_channel('512765323116806158'), 'Correct, good job!')
                    global points
                    points += 1
                    print(points)
                    await get_question()
                    
                elif answer.content != pname:
                    time.sleep(0.5)
                    await client.send_message(client.get_channel('512765323116806158'), f'Incorrect! The correct answer was {pname}')
                    await client.send_message(client.get_channel('512765323116806158'), f'you got {points} correct answers')
            else:
                await client.send_message(client.get_channel('512765323116806158'), f'Ran out of time! The correct answer was {pname}')
                await client.send_message(client.get_channel('512765323116806158'), f'you got {points} correct answers')
        global points
        points = 0
        await get_question()
