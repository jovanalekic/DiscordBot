'''
main file for the bot
'''
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

# get all theme urls from pageNames.txt
theme_url_list = []
page_names_file_string = "pageNames.txt"
page_names_file = open(page_names_file_string, "r")

# use the blacklist to filter out bad theme urls
page_blacklist_file_string = "pageNamesBlacklistCleaned.txt"
page_blacklist_file = open(page_blacklist_file_string, "r")

# 2 arrays: 1 of all the themes, 1 of the blacklisted themes
theme_url_list = page_names_file.read().split("\n")
theme_url_blacklist = page_blacklist_file.read().split("\n")
  
# array of colors, types, and categories 
colorlist = [
  "red",
  "orange",
  "tangerine",
  "red-orange",
  "yellow",
  "lime",
  "forest green",
  "aqua",
  "navy",
  "blue",
  "sky blue",
  "purple",
  "violet",
  "lavender",
  "baby pink",
  "hot pink",
  "magenta",
  "white",
  "beige",
  "brown",
  "black",
  "light gray",
  "dark gray"
]

kanditypelist = [
  "panel",
  "charm",
  "single",
  "double",
  "x-based",
  "star",
  "flower cuff",
  "carousel cuff",
  "double carousel cuff",
  "slinky cuff",
  "3d cuff",
  "ladder cuff",
  "3d ladder cuff",
  "rotater cuff",
  "peyote",
  "multistitch"  
]

perlertypelist = [
  "2d perler",
  "3d perler"
]

categorylist = [
  "perler",
  "kandi"
]

# confirm the bot is online
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

# get a random theme from the theme list
def get_random_theme():
   return random.choice(theme_url_list)

# removes all identical themes from blacklist from the theme array
# i.e. clean the theme array
def clean_theme_array():
  for i in theme_url_list:
    if i in theme_url_blacklist:
      theme_url_list.remove(i)

# returns a formatted string with a random theme for the user
def get_random_theme_message_string():
  return "Here's a random theme for you:\n" + get_random_theme()

# listens for messages and if the message has a command in it, the bot will respond
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  formatted_message = message.content.lower()
  
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
  #help message
  if formatted_message == "$kandihelp":
    
    help_message_file = open("helpMessage.txt")
    help_message_string = help_message_file.read()
    await message.channel.send(help_message_string)
  
  #if the user types in $category, they will get either kandi or perler
  if formatted_message.startswith('$category'):
    #num = random.random()
    '''
    #category_to_send = ""
    if (num<=.5):
      #category_to_send = 'perler'
    else:
      #category_to_send = 'kandi'
    '''
    randomcategory=random.choice(categorylist)
    await message.channel.send(randomcategory)

  #if the user types in $kandi
  #$kandi color theme type valid - will output on whichever user chooses to put in
  if formatted_message.startswith('$kandi '):
    
    # string to send
    string_to_send = "Kandi: \n"
    orig_string = string_to_send
    allArgument = formatted_message.find("all") != -1
    
    #check if the user typed "color", then give them a random color
    if formatted_message.find("color")!=-1 or allArgument:
      #want to get a random index and print from the color list at that index
      randomkandicolor=random.choice(colorlist)
      string_to_send += "Color: " + randomkandicolor + "\n"
      
    #check if the user typed "type", then give them a random type
    if formatted_message.find("type")!=-1 or allArgument:
      randomkanditype=random.choice(kanditypelist)
      string_to_send += "Type: " + randomkanditype + "\n"
      
    #check if the user typed "theme", then give them a random theme
    if formatted_message.find("theme")!=-1 or allArgument:
      string_to_send += get_random_theme_message_string() + "\n"
      
    if(string_to_send == orig_string):
      string_to_send = "guys you gotta specify either \"color\", \"type\", \"theme\", or \"all\" after $kandi"
      
    await message.channel.send(string_to_send)
    
    
  #if the user types in $perler
  #$perler color theme type valid - will output on whichever user chooses to put in
  if formatted_message.startswith('$perler '):
    
    # string to send in message
    string_to_send = "Perler: \n"
    orig_string = string_to_send

    allArgument = formatted_message.find("all") != -1
    
    #check if the user typed "color", then give them a random color"
    if formatted_message.find("color")!=-1 or allArgument:
      randomperlercolor=random.choice(colorlist)
      string_to_send += "Color: " + randomperlercolor + "\n"
      
    #check if the user typed "type", then give them a random type
    if formatted_message.find("type")!=-1 or allArgument:
      randomperlertype=random.choice(perlertypelist)
      string_to_send += "Type: " + randomperlertype + "\n"
    
    #check if the user typed "theme", then give them a random theme
    if formatted_message.find("theme")!=-1 or allArgument:
      string_to_send += get_random_theme_message_string() + "\n"
      
    if(string_to_send == orig_string):
      string_to_send = "guys you gotta specify either \"color\", \"type\", \"theme\", or \"all\" after $perler"

    await message.channel.send(string_to_send)
  
    

# runs the bot using our Discord API token
client.run('MTIxMDcyOTcxNzQ4MTYxMTMyNg.GgUFnC.1zJcfyiV4ug6qOI61j1kHL7Wr3vv4VNZ5PfKyE')