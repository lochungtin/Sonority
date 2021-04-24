import discord
from discord.ext import commands
from discord.ext.commands import Bot

class CogExt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
def setBot(botIn: commands.Bot):
    global bot
    bot = botIn
