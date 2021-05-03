import os
import discord
from discord.ext import commands    
from dotenv import load_dotenv
from forex_python.converter import CurrencyRates

# .env file 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot
client = commands.Bot(command_prefix = "!")

# Currency
c = CurrencyRates()

# Current Currency with forex_python.conventer
def current(x: str, y: str):
    return c.get_rate(x, y)

# Convert Currency with forex_python.conventer 
def convert(x: str, y: str, z: float):
    converted = c.convert(x, y, z)
    return converted

def rando(x: int, y: int):
    return random.randint(x, y)

@client.event
async def on_ready():
    print(f"{client.user.name} is online...")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channel, name = "welcome")
    await channel.send(f"{member} is joined the discord channel.")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You con't do that.")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguments.")
        await ctx.message.delete()
    else:
        raise error

@client.command()    
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.command()
async def curr(ctx, from_to_country: str = "", amount: int = 1):
    embed = discord.Embed(title = "CURRENT CURRENCIES", color = discord.Colour.green())
    embed.add_field(name="USD", value=current("USD", "TRY"))
    embed.add_field(name="EUR", value=current("EUR", "TRY"))
    if from_to_country != "" and amount != 1:
        a,b = from_to_country.split("-")
        a.upper(),b.upper()
        if a == "USD":
            embed.add_field(name="USD to TRY", value=convert(a, b, amount))
        else: 
            embed.add_field(name="EUR to TRY", value=convert(a, b, amount))
    embed.set_footer(text="by Forex")
    await ctx.send(embed=embed)

@client.command()
async def rand(ctx, x:int, y:int):
    res = rando(x ,y)
    await ctx.send(res)

if __name__ == "__main__":
    for filename in os.listdir("/home/abdullah/Desktop/Discord/Discord/cogs"):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f"{filename} loaded")


client.run(TOKEN)
