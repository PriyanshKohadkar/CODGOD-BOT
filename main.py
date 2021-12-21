import discord
import os
from keep_alive import keep_alive
client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('hello!')
  elif message.content.startswith('hi'):
    await message.channel.send('whatsup!')  
  elif message.content.startswith('$syllabus'):
    await message.channel.send("syllabus hasn't been uploaded yet! stay tune!")
  elif  message.content.startswith('$examdate'):
    await message.channel.send('the upcoming exam is going to be a preparetory! \n exam date: 17th january 2022!')
  elif  message.content.startswith('commands'):
    await message.channel.send("some simple commands for the  <@922523913446096999> \n $syllabus :- for the syllabus \n $examdate :- exam date")
  elif   message.content.startswith('$developer'):
    await message.channel.send("This bot is developed and made by:- \n <@646008825224364042> \n github profile:- https://github.com/gunshotop \n replit.com:- https://replit.com/@Gunshotgaming \n discord tag:- CODEGOD</>#5307 \n discord id:- '646008825224364042'") 
my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)