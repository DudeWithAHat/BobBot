import discord
from discord.ext import commands
import secret_key

intents = discord.Intents.default()
intents.message_content=True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Who goes there?!?")

bot.run(secret_key.token)
