import discord
from discord.ext import commands
import requests
import random
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot Online!")
    await client.change_presence(activity=discord.Activity(name="Roblox Police Simulator",type=discord.ActivityType.playing))

bad_words = ["fuck","shit","bitch","cunt","pussy","ass","dick","damn","heck"]
responses = ['wow, you really would use that language in this christian discord server.', 'ayo homie chill with that', 'bruh...', 'lets calm down there buster', 'dude, really?']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content==('!hello'):
        await message.channel.send('play roblox with me or die')
    if message.content==('!ping'):
        await message.channel.send('pong')
    for each in bad_words:
            if each in message.content:
                await message.channel.send(random.choice(responses))

client.run("process.env.BOT_TOKEN")
