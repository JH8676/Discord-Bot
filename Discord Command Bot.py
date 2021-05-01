import discord
import time
import asyncio
from discord.ext import commands
import os
import random

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.command(name='insult', help="Format: <user><amount of times>")
#@commands.has_role("Pog Champ")
async def insult_user(ctx, member: discord.Member, repeats=1):
    repeats = int(repeats)

    insults = [f"{member.mention} stfu you fat prick", f"{member.mention} you're a cunt", f"{member.mention} imagine checking this mention dumbass"]

    response = random.choice(insults)

    for x in range(repeats):
        await ctx.send(response)

@bot.command(name='repeat')
async def repeat_phrase(ctx, phrase, repeats=1):
    repeats = int(repeats)

    for x in range(repeats):
        await ctx.send(phrase)

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.errors.CheckFailure):
#         await ctx.send(f'{message.author.mention}You do not have the correct role for this command.')

@bot.command(name='kill', help="Kicks user from Server")
@commands.has_role("Pog Champ")
async def kill_users(ctx, member: discord.Member):
    await ctx.send(f"Lining {member.mention} up in my sights")
    await member.kick(reason="You got sniped")

bot.run(token)