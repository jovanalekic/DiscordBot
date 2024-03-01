import random
import aiohttp
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

'''
helpFile = open("kandiHelp.txt", "r")
themesFile = open("kandiThemes.txt", "r")
kandiTypesFile = open("kandiTypes.txt", "r")
kandiColorsFile = open("kandiColors.txt", "r")
'''

theme_list = [
  "cottage core", 
  "cyberpunk", 
  "steampunk", 
  "futuristic", 
  "forest", 
  "stars",
  "outer space", 
  "horror", 
  "hot dog",
  "frutiger aero", 
  "frutiger metro",
  "cybergoth",
  "dark academia",
  "sanrio",
  "kidcore",
  "farmcore",
  "fruit",
]


async def get_random_aesthetic_url():
  session = aiohttp.ClientSession()
  response = await session.get("http://aesthetics.fandom.com/wiki/Special:Random")
  url = response.url
  return url 

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  formatted_message = message.content.lower()

  if formatted_message.startswith('$randomaesthetic'):
    await message.channel.send(get_random_aesthetic_url())
  
  '''
  on message 
    
    if message starts with "$kandi"
      
      if message contains "color"
        add random color to output
      if message contains "type"
        add random type to output
      if message contains "theme"
        add random theme to output
      ...

    For now, these formats are valid:  
    $kandicolortypetheme
    $kandi color type theme
    $kandi color typetheme
    $kandi colorthemetype
      
    if message starts with "$perler"
      if message contains "color"
        add random color to output
      ...
  '''
  #if the user types in $category, they will get either kandi or perler
  if formatted_message.startswith('$category'):
    num=random.random()
    if (num<=.5):
      await message.channel.send('perler')
    else:
      await message.channel.send('kandi')
  
  if formatted_message.startswith('$theme'):
    choice = random.choice(theme_list)
    await message.channel.send('chosen theme: ' + choice)
    

#if the user types in $kandi
  if formatted_message.startswith('$kandi'):
    #check if the user typed "color"
    #if formatted_message
    await message.channel.send('')
    '''
      read the file kandiTypes 
      build a list of strings, separated by the "/n" character
        {single, double, charm, panel, ...}
      return random element from that list
    '''
    #randomvar=getrandomnumber()  
    
 # if formatted_message.startswith('$'):  
  #peepee poopoo
 
client.run('MTIxMDcyOTcxNzQ4MTYxMTMyNg.GGT_Dw.eb0hsiYAKYvr3hRp-oPImhRF4BmXGbNqnKqWBQ')