import os
import discord
from datetime import datetime
from discord.ext import commands
from dotenv import dotenv_values
config = dotenv_values(".env")

owners = (config["OWNER"])

bot = commands.Bot(
    command_prefix="s.",
    help_command=None,
    owner_ids=owners
)

@bot.event
async def on_ready():
    # login console output
    print("BOT ONLINE - {}".format(bot.user))

@bot.event
async def on_message(msg):
    # ignore own messages
    if msg.author == bot.user:
        return

    if msg.content.startswith("s."):
        await bot.process_commands(msg)
    
    return

for filename in os.listdir("cmds"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cmds.{filename[:-3]}")
            print("EXT LOADED - {}".format(filename))
        except Exception as err:
            print("EXT FAILED - {} | {}".format(filename, traceback.format_exception_only(err.__class__, err)[0]))
            print("Stack: ", exc_info=True) 

bot.run(config["TOKEN"])