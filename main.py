import discord, os
from dotenv import dotenv_values
config = dotenv_values(".env")

client = discord.Client()

@client.event
async def on_ready():
    # login console output
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(msg):
    # ignore own messages
    if msg.author == client.user:
        return

    if msg.content.startswith("$ping"):
        await msg.channel.send("pong")

client.run(config["TOKEN"])