import discord, asyncio, random, time, json, os, string
from discord.ext import commands
from discord.utils import get

class Ratio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Ratio someone")
    async def ratio(self,ctx,msg: discord.Message):
        ratio = await msg.reply("ratio")
        await ctx.respond(content="done", ephemeral=True)
        await ratio.add_reaction("<:up:1025621241329106965>")
        await ratio.add_reaction("<:down:1025621239995314226>")

def setup(bot):
    bot.add_cog(Ratio(bot))