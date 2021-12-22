import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "sed", "angry", "depressing", "miserable", "fucked up",]

starter_encouragements = [
"cheer up!",
"hang in there",
"you are a great person!",
"don't forget you are a sigma male!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]  
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
   
  
@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

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

  if  message.content.startswith('$examdate'):
    await message.channel.send('the upcoming exam is going to be a preparetory! \n exam date: 17th january 2022! \n exam mode:- online(may change later depending upon current situation)')

  if  message.content.startswith('commands'):
    await message.channel.send("some simple commands for the  <@922523913446096999> \n $developer :- for developer information \n $responding true(for responding on) and $responding false(for responding off) \n $syllabus :- for the syllabus \n $examdate :- exam date \n $inspire :- for getting inspiration Quotes! \n $listencourage :- for getting current encouragement list \n $newencourage :- to add a newencouragement(ex. you are best! don't be sad) \n $delencourage :- for deleting encouragement messages (note:- the list start with 0, not with 1 index)")

  if   message.content.startswith('$developer'):
    await message.channel.send("This bot is developed and made by:- \n <@646008825224364042> \n github profile:- https://github.com/gunshotop \n replit.com:- https://replit.com/@Gunshotgaming \n Youtube channel:- https://www.youtube.com/channel/UC5Bf0ZVk7qi_CS1b15va6qw \n instagram profile:- https://www.instagram.com/gunshot.ig/ \n discord tag:- CODEGOD</>#5307 \n discord id:- '646008825224364042'")

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = db["encouragements"]
      
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$newencourage"):
    encouraging_message = msg.split("$newencourage ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("new encouraging message added!")

  if msg.startswith("$delencourage"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$delencourage",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
      await message.channel.send(encouragements)

  if msg.startswith("$listencourage"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
      await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)