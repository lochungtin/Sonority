import os
import discord
from datetime import datetime
from discord.ext import commands
from dotenv import dotenv_values
config = dotenv_values(".env")

owners = (config["OWNER"])

client = commands.Bot(
    command_prefix="s.",
    help_command=None,
    owner_ids=owners
)

@client.event
async def on_ready():
    # login console output
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(msg):
    # ignore own messages
    if msg.author == client.user:
        return

    if msg.content.startswith("s."):
        await client.process_commands(msg)
    
    return
        

client.run(config["TOKEN"])