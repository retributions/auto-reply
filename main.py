import discord, random, asyncio, os, colorama, datetime
from colorama import Fore
from colorama import Fore as C
from discord.ext import commands
os.system('clear')

token = ""

client = commands.Bot(command_prefix='')
client.remove_command('help')

@client.event
async def on_ready():
  print(f'ready')
  os.system('clear')

@client.event
async def on_message(message):
  if isinstance(message.channel, discord.TextChannel):
   if "nigger" in message.content.lower():
    await message.channel.send(message.author.mention + " Don't Say That <a:x_:794322832786980864>")
    print(f'{C.WHITE}[{C.LIGHTBLACK_EX}{datetime.datetime.now()} UTC{C.WHITE}]\n{C.WHITE}CHANNEL: {C.LIGHTBLACK_EX}{message.channel.name}\n{C.WHITE}SERVER: {C.LIGHTBLACK_EX}{message.guild.name}\n{C.WHITE}AUTHOR: {C.LIGHTBLACK_EX}{message.author}\n{C.WHITE}MESSAGE: {C.LIGHTBLACK_EX}{message.content}\n')
    await message.add_reaction('<a:x_:794322832786980864>')
   elif "nigga" in message.content.lower():
    await message.channel.send(message.author.mention + " Don't Say That <a:x_:794322832786980864>")
    print(f'{C.WHITE}[{C.LIGHTBLACK_EX}{datetime.datetime.now()} UTC{C.WHITE}]\n{C.WHITE}CHANNEL: {C.LIGHTBLACK_EX}{message.channel.name}\n{C.WHITE}SERVER: {C.LIGHTBLACK_EX}{message.guild.name}\n{C.WHITE}AUTHOR: {C.LIGHTBLACK_EX}{message.author}\n{C.WHITE}MESSAGE: {C.LIGHTBLACK_EX}{message.content}\n')
    await message.add_reaction('<a:x_:794322832786980864>')
  elif isinstance(message.channel, discord.GroupChannel):
   if "nigger" in message.content.lower():
    await message.channel.send(message.author.mention + " Don't Say That <a:x_:794322832786980864>")
    print(f'{C.WHITE}[{C.LIGHTBLACK_EX}{datetime.datetime.now()} UTC{C.WHITE}]\n{C.WHITE}CHANNEL: {C.LIGHTBLACK_EX}{message.channel.name}\n{C.WHITE}AUTHOR: {C.LIGHTBLACK_EX}{message.author}\n{C.WHITE}MESSAGE: {C.LIGHTBLACK_EX}{message.content}\n')
    await message.add_reaction('<a:x_:794322832786980864>')
   elif "nigga" in message.content.lower():
    await message.channel.send(message.author.mention + " Don't Say That <a:x_:794322832786980864>")
    print(f'{C.WHITE}[{C.LIGHTBLACK_EX}{datetime.datetime.now()} UTC{C.WHITE}]\n{C.WHITE}CHANNEL: {C.LIGHTBLACK_EX}{message.channel.name}\n{C.WHITE}AUTHOR: {C.LIGHTBLACK_EX}{message.author}\n{C.WHITE}MESSAGE: {C.LIGHTBLACK_EX}{message.content}\n') 

client.run(token, bot=False, reconnect=True)
