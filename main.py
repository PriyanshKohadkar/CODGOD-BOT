import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
import music

client = discord.Client(commands_prefix="$")
cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup(client)



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
  await client.change_presence(status=discord.Status.online, activity=discord.Game("$Ghelp"))
  print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.mention_everyone:
    return
  else:
    if client.user.mentioned_in(message):
      await message.channel.send('I am here to help you!')  
  msg = message.content

  if message.content.lower().startswith('hello'):
    await message.channel.send('hello! I am here to help you!')

  if message.content.lower().startswith('hi'):
    await message.channel.send('whatsup!')
  if message.content.lower().startswith("umai"):
    await message.channel.send('Umai!')

  if message.content.lower().startswith("thanks @Pythbot"):
    await message.channel.send("welcome happy to help you!")
  if message.content.lower().startswith("thank you <@923611772135546960>"):
    await message.channel.send("welcome happy to help you!")
  if message.content.lower().startswith("ok <@923611772135546960>"):
    await message.channel.send("done!")  
  if message.content.lower().startswith('$syllabus sst'):
    await message.channel.send("```GEOGRAPHY:- \n 1. Resources:Utilisation and Development \n 2.Natural resources:Land,Soil,Water \n 3.Natural resorces:Vegetation and Wildlife \n 4.Agriculture \n 5. Human Resources \n HISTORY:- \n 1.Modern Period \n 2.Establishment of Company Rule in India \n 3.Colonialism:Rural and Tribal socities \n 4. The First war of Independence -1857 \n 5.The nationalist movement(1870 to 1947)\n 6.India marches ahead \n CIVICS:- \n 1.Our Constitution \n 2.Fundamental rights ,Fundamental Duties and Directive Principles of State Policy \n 3.The Union Government: The legislature \n 4.The Union Government: The Executive \n 5.The Union Government:The Judiciary```")
  
  if message.content.lower().startswith('$send mark_scheme'):
    await message.channel.send("https://drive.google.com/file/d/1efqQQb9ZwuimTHyuszrEruiDpZJBNAT2/view?usp=sharing")

  if message.content.lower().startswith('$send sample_papers'):
    await message.channel.send("https://drive.google.com/file/d/1kWBrIjGjfNbCFshDK091vj0x2v-A4Z6W/view?usp=sharing") 

  if message.content.lower().startswith('$send'):
    await message.channel.send("```to get notes of any subjects type '$send <subject name>' (exclusives:- $send mark_scheme, $send sample_papers)```")
  if message.content.lower().startswith('$syllabus science'):
    await message.channel.send("syllabus has'nt been  uploaded yet")

  if message.content.lower().startswith('$syllabus'):
    await message.channel.send("to get syllabus of any subject type '$syllabus <subject name>'")

  if  message.content.lower().startswith('$examtable'):
    await message.channel.send('```the upcoming exam is going to be a preparetory! \n exam date: 17th january 2022! \n exam mode:- online(may change later depending upon current situation)``` \n ```(sr.no, date, day, subject format) \n 1. 17.01.2022 Monday English \n 2. 19.01.2022 Mathematics Wednesday \n 3. 21.01.2022 Friday Hindi \n 4. 24.01.2022 Monday Social Science \n 5. 27.01.2022 Thursday Science \n 6. 29.01.2022 Saturday Sanskrit / Marathi \n 7. 31.01.2022 Monday Moral Education``` \n ```1. The timing of examination shall be from 8.00 am to 11.00 am. \n 2. Students to be ready 10 minutes prior to the examination schedule. \n 3. Click clear image of answer sheets and convert images in a single pdf before uploading the subjective paper. \n 4. Please write your name, section and roll number on every page of answer sheet of your subjective paper. \n 5. Follow the instructions strictly and in case of any difficulty contact your class teacher. \n . In case if there is any change from the current situation we shall reschedule the mode, date and time of the examination and will be intimated.```\n  to get the image pls visit:- \n https://drive.google.com/file/d/1PN-DhPQsXiolIWWF5nwHToPV9BOX4JEf/view?usp=sharing \n download image from here ')

  if  message.content.lower().startswith('commands'):
    await message.channel.send("```some simple commands for the Pythobot:- \n $developer :- for developer information \n $responding true(for responding on) and $responding false(for responding off) \n $syllabus :- for the syllabus \n $examdate :- exam date \n $inspire :- for getting inspiration Quotes! \n $listencourage :- for getting current encouragement list \n $newencourage :- to add a newencouragement(ex. you are best! don't be sad) \n $delencourage :- for deleting encouragement messages (note:- the list start with 0, not with 1 index)```")

  if  message.content.lower().startswith('$ghelp'):
    await message.channel.send("```some simple commands for the Pythbot:- \n $developer :- for developer information \n $responding true(for responding on) and $responding false(for responding off) \n $syllabus :- for the syllabus \n $examdate :- exam date \n $inspire :- for getting inspiration Quotes! \n $listencourage :- for getting current encouragement list \n $newencourage :- to add a newencouragement(ex. you are best! don't be sad) \n $delencourage :- for deleting encouragement messages (note:- the list start with 0, not with 1 index) \n $send :- for getting notes of any subject or exam related```")

  if  message.content.lower().startswith('$developer'):
    await message.channel.send("This bot is developed and made by:- \n <@646008825224364042> \n github profile:- https://github.com/gunshotop \n replit.com:- https://replit.com/@Gunshotgaming \n Youtube channel:- https://www.youtube.com/channel/UC5Bf0ZVk7qi_CS1b15va6qw \n instagram profile:- https://www.instagram.com/gunshot.ig/ \n discord tag:- CODEGOD</>#5307 \n discord id:- '646008825224364042'")

  if message.content.lower().startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = db["encouragements"]
      
    if any(word in msg.lower() for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.lower().startswith("$newencourage"):
    encouraging_message = msg.split("$newencourage ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("new encouraging message added!")

  if msg.lower().startswith("$delencourage"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$delencourage",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
      await message.channel.send(encouragements)

  if msg.lower().startswith("$listencourage"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
      await message.channel.send(encouragements)

  if msg.lower().startswith("$responding"):
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