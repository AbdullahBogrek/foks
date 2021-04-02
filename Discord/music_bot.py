import os
import discord
import youtube_dl
from discord.ext import commands
from dotenv import load_dotenv

# .env file 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print(f"{client.user.name} is online...")

@client.command()
async def play(ctx, url: str):
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name = "party")
    voice = discord.utils.get(client.guilds.voice_clients, guild = ctx.guilds)
    player = await voice.create_ytdl_player(url)
    players[voice_channel.id] = player
    player.start()
    # if not voice.is_connected():
    #     await voice_channel.connect()

@client.command()
async def leave(ctx):
    voice = discord.guild.get(ctx.guild.voice_clients, guild = ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is already not connected to {voice.channel.name}.")

@client.command()
async def pause(ctx):
    voice = discord.guild.get(ctx.guild.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("No audio is playing.")  

@client.command()
async def resume(ctx):
    voice = discord.guild.get(ctx.guild.voice_clients, guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio already is playing")

@client.command()
async def stop(ctx):    
    voice = discord.guild.get(ctx.guild.voice_clients, guild = ctx.guild)
    voice.stop()


client.run(TOKEN)   

