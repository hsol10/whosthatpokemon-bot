from keep_alive import keep_alive
import discord
import os
import time
from pokemon import pokemon
import random
global fisrt_place_player
global p2p
global p3p
p1p = 'gnha'
p2p = 'grdfahgr'
p3p = 'hgraehrfd'
global p1
global p2
global p3
p1 = 5
p2 = 3
p3 = 1

client = discord.Client()

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
                    await client.send_message(client.get_channel('512765323116806158'), 'correct, good job!')
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

        global p3
        global p2
        global p1
        global p1p
        global p2p
        global p3p
        
        if points > p3 and points < p2:
            global p3p
            p3p = message.author
            p3 = points
            await client.send_message(client.get_channel('512765323116806158'), 'congratualtions you got third place on the leaderboard')
        elif points > p2 and points < p1:
            global p2p
            p3p = p2p
            p3 = p2
            p2p = message.author
            p2 = points
            await client.send_message(client.get_channel('512765323116806158'), 'congratulations you got second place on the leaderboard')
        elif points > p1:
            global fisrt_place_player
            p3p = p2p
            p3 = p2
            p2p = p1p
            p2 = p1
            p1p = message.author
            p1 = points
            await client.send_message(client.get_channel('512765323116806158'), 'congratualtions you got first place on the leaderboard')
        
    elif message.author != client.user and message.content.startswith('$lb'):
        lb = discord.Embed(title = 'Leaderboard', description = f'''
        1st place: {p1p} score: {p1}
        2nd place: {p2p} score: {p2}
        3rd place: {p3p} score: {p3}
        ''')
        await client.send_message(message.channel, embed=lb)

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
