import os
import discord
from discord.ext import commands    
from dotenv import load_dotenv
from google_currency import convert  
from forex_python.converter import CurrencyRates

# .env file 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Currency
c = CurrencyRates()

# Bot
client = commands.Bot(command_prefix = "!")

# Current Currency with forex_python.conventer
def current(x: str, y: str):
    return c.get_rate(x, y)

# Convert Currency with google_curreny 
def convert(x: str, y: str, z: float):
    return convert(x, y, z) 

@client.event
async def on_ready():
    print(f"{client.user.name} is online...")

@client.command()
async def doviz(ctx):
    embed = discord.Embed(title = "CURRENT CURRENCIES", color = discord.Colour.green())
    embed.add_field(name="USD", value=current("USD", "TRY"))
    embed.add_field(name="EUR", value=current("EUR", "TRY"))
    embed.set_footer(text="by Forex")
    await ctx.send(embed=embed)

@client.command()
async def cevir(ctx, from_to_country: str, amount: float):
    embed = discord.Embed(title = "CONVERTED CURRENCY", color = discord.Colour.green())
    embed.add_field(name="USD", value=current("USD", "TRY"))
    embed.add_field(name="EUR", value=current("EUR", "TRY"))
    a,b = from_to_country.split("-")
    embed.add_field(name="EUR to TRY", value=convert(a, b, amount))
    embed.add_field(name="USD to TRY", value=convert(a, b, amount))
    embed.set_footer(text="by Forex and Google")
    await ctx.send(embed=embed)

client.run(TOKEN)