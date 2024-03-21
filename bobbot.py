import discord
from discord.ext import commands
import secret_key
import random

intents = discord.Intents.default()
intents.message_content=True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def poke(ctx):
    quotes = ["Citizen.",
              "Move along.",
              "Who goes there?!",
              "Halt.",
              "Traveler.",
              "Keep your nose clean, citizen.",
             "If you're traveling outside the city, you watch yourself, ya hear?",
             "It's a peaceful day. Don't go and change that on my watch."]
    await ctx.send(random.choice(quotes))

@bot.command()
async def say(ctx, arg):
   await ctx.send(arg)

bot.run(secret_key.token)
