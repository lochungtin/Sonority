import asyncio
from discord.ext import commands
from utils.cogext import CogExt, setBot
from utils.logger import Logger

class Scheduler(CogExt):

    # test ping command
    @commands.command()
    async def ping(self, ctx):
        Logger.debug("{} issued a ping command".format(ctx.author))
        await ctx.send("{} pong".format(ctx.message.author.mention))

    

# extension binding to bot
def setup(bot):
    bot.add_cog(Scheduler(bot))
    setBot(bot)
    
