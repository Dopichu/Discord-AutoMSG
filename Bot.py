import discord,asyncio,os
from discord.ext import commands, tasks


client = discord.Client()



@client.event
async def on_ready():
    print('Bot is ready.') #Bot rdy
    


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #Should print but dk whas wrong cba to fix
    




@client.event
async def on_message(message):
  if message.author ==client.user: #Doesn't respond to itself
    return

  if message.content.startswith('Wsup') :
      await message.channel.send('Hello') #Responds with Hello





@tasks.loop(minutes=5) #Loops code every minute
async def test():
    channel = client.get_channel(ChannelID) #Channel id is you guessed it, channel id
    await channel.send("insert message") #The message it sends every minute"

@client.event
async def on_ready():
    test.start() #Starts the loop
  
client.run(os.getenv("token")) #token
