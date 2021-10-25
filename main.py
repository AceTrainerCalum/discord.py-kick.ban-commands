# imports
import discord
from discord.ext import commands, tasks

#set the client
client = commands.Bot(command_prefix="T!")

@client.command(name="kick", help="kicks a user) #client command
async def kick(ctx, member = discord.member, *, reason = None):

  if reason == None:
    reason = F"{ctx.author} gave no reason given"

  try:
    member.kick(reason = reason)
    await ctx.send(F"Sucsesfully kicked {member}")
  except:
    await ctx.send("there was a problem")

@client.command(name="ban", help="bans a user") # client command
async def ban(ctx, member = discord.member, *, reason = None):

  if reason == None:
    reason = f"{ctx.author} gave no reason"
  try:
    member.ban(reason = reason)
    await ctx.send(F"Sucsesfully baned {member}")
  except:
    await ctx.send("there was a problem")
    
client.run("your token here")
