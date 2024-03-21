import discord
from discord.ext import commands
import secret_key
import random
import nodcount

intents = discord.Intents.default()
intents.message_content=True

bot = commands.Bot(command_prefix='/', intents=intents)

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

@bot.command()
async def version(ctx):
   await ctx.send("Version 1.0.2 (Added Nod Counter)")

@bot.command()
async def addnod(ctx, arg):
   nodcount.increment(arg)
   await ctx.send(f"Aye. Adding a notch to the counter for \"{arg}\".")

@bot.command()
async def displaynods(ctx):
   await ctx.send(f"Aye. Pulling out the latest scores. . .")
   list = ""
   for name, count in nodcount.select():
      list += f"- {name}: {count} nods\n"
   await ctx.send(list)


bot.run(secret_key.token)
