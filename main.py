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
  if message.content.startswith('$syllabus sst'):
    await message.channel.send("GEOGRAPHY:- \n 1. Resources:Utilisation and Development \n 2.Natural resources:Land,Soil,Water \n 3.Natural resorces:Vegetation and Wildlife \n 4.Agriculture \n 5. Human Resources \n HISTORY:- \n 1.Modern Period \n 2.Establishment of Company Rule in India \n 3.Colonialism:Rural and Tribal socities \n 4. The First war of Independence -1857 \n 5.The nationalist movement(1870 to 1947)\n 6.India marches ahead \n CIVICS:- \n 1.Our Constitution \n 2.Fundamental rights ,Fundamental Duties and Directive Principles of State Policy \n 3.The Union Government: The legislature \n 4.The Union Government: The Executive \n 5.The Union Government:The Judiciary")
  if message.content.startswith('$syllabus science'):
    await message.channel.send("syllabus has'nt been  uploaded yet")
  if message.content.startswith('$syllabus'):
    await message.channel.send("to get syllabus of any subject type '$syllabus <subject name>'")   
  elif  message.content.startswith('$examdate'):
    await message.channel.send('the upcoming exam is going to be a preparetory! \n exam date: 17th january 2022!')
  elif  message.content.startswith('commands'):
    await message.channel.send("some simple commands for the  <@922523913446096999> \n $syllabus :- for the syllabus \n $examdate :- exam date")
  elif   message.content.startswith('$developer'):
    await message.channel.send("This bot is developed and made by:- \n <@646008825224364042> \n github profile:- https://github.com/gunshotop \n replit.com:- https://replit.com/@Gunshotgaming \n Youtube channel:- https://www.youtube.com/channel/UC5Bf0ZVk7qi_CS1b15va6qw \n instagram profile:- https://www.instagram.com/gunshot.ig/ \n discord tag:- CODEGOD</>#5307 \n discord id:- '646008825224364042'") 
my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)