import discord, asyncio, random, time, json, os, string
from discord.ext import commands

f = open('config.json')
config = json.load(f)

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Evaluate some code")
    async def e(self, ctx:discord.ApplicationContext, *, code):
        if ctx.author.id in config["OWNER"]:
            try:
                res = await eval(code)
                await ctx.respond(f"```html\n{res}\n```")             
            except Exception as e:
               await ctx.respond(f"**Error:** ```\n{e}\n```")
        else:
            await ctx.respond(f"**Error:** ```u got no dev perms lol```")
            
    @commands.slash_command(description="See the ping of the bot")
    async def ping(self, ctx):
        await ctx.respond(f"Pong 🏓 **|** `{round(self.bot.latency * 1000)}ms`")

def setup(bot):
    bot.add_cog(Dev(bot))