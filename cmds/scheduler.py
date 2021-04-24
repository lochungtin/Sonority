from discord.ext import commands
from utils.cogext import CogExt, setBot

class Scheduler(CogExt):

    @commands.command()
    async def test(self, ctx, arg):
        await ctx.send(arg)

# extension binding to bot
def setup(bot):
    bot.add_cog(Scheduler(bot))
    setBot(bot)
    
