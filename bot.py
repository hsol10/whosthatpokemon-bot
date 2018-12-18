from keep_alive import keep_alive
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        with open('250px-001Bulbasaur.png', 'rb') as f:
            await client.send_file(client.get_channel, f)

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
