import asyncio
import discord
from discord.ext import commands
from utils.cogext import CogExt, setBot
from utils.logger import Logger

timeUnitMlp = [1, 60, 3600, 86400]

class Scheduler(CogExt):

    # test ping command
    @commands.command()
    async def ping(self, ctx):
        Logger.debug("{} issued a ping command".format(ctx.author))
        await ctx.send("{} pong".format(ctx.message.author.mention))

    # schedule ping
    @commands.command()
    async def timer(self, ctx, time, *args):
        timeArr = time.split(":")
        timeArgs = len(timeArr)
        totalSecs = 0
        
        # invalid timecode
        if (timeArgs > 4):
            errEmbed = discord.Embed(
                color=discord.Colour.magenta(),
                title="Error: Invalid Timecode",
                description="""
                    Timecode Format: `d*:h*:m*:s+`
                    `*` meaning 0 or more digits
                    `+` meaning 1 or more digits
                """
            )
            await ctx.send(embed=errEmbed)
            Logger.debug("Invalid timecode received - no timers scheduled")
            return 
        
        for i in range(0, timeArgs):
            totalSecs += (int(timeArr[(timeArgs - 1) - i]) * timeUnitMlp[i])

        Logger.debug("{} issued a set timer command. Timer will expire in {}s".format(ctx.author, totalSecs))
        
        pingChannel = "Universal"
        pingChannelID = ""

        # parse args
        text = ""
        if (len(args) > 0):
            if args[0].startswith("-"):
                # has modifier
                if args[0].lower()[1] == 'm':
                    Logger.debug("Timer ping will be issued in the mobile only ping channel")
                    pingChannel = "Mobile"
                    pingChannelID = ""
                elif args[0].lower()[1] == 'd':
                    Logger.debug("Timer ping will be issued in the desktop only ping channel")
                    pingChannel = "Desktop"
                    pingChannelID = ""
                else:
                    Logger.debug("Timer ping will be issued in the universal ping channel")
            else:
                Logger.debug("Timer ping will be issued in the universal ping channel")
            
            text = " ".join(args[args[0].startswith("-") * 1:])
        
        # send response message to schedule request
        responseEmbed = discord.Embed(
            color = discord.Colour.teal(),
            title="Timer set",
            description="""
                Your timer as been set
                Duration: `{}s`
                Ping Channel: `{}`
            """.format(totalSecs, pingChannel)
        )
        await ctx.send(embed=responseEmbed)

        # wait
        await asyncio.sleep(totalSecs)
        
        # times up, send alarm
        timesupEmbed = discord.Embed(
            color = discord.Colour.teal(),
            title="Times Up",
            description="""
                Your timer for `{}s` has ended
                Event Desciption: {}
            """.format(totalSecs, text)
        )
        await ctx.send(ctx.message.author.mention)
        await ctx.send(embed=timesupEmbed)

# extension binding to bot
def setup(bot):
    bot.add_cog(Scheduler(bot))
    setBot(bot)
    