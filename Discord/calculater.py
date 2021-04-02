# bot.py
import os
import math
import random
import discord
from discord.ext import commands    
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = "!", help_command =None)

def subtract(x: float, y: float):
    return x - y

def addition(x: float, y: float):
    return x + y

def divide(x: float, y: float):
    return x / y

def random(x: int, y: int):
    return random.randint(x, y)

def square(x: float):
    return math.sqrt(x)

# def sinus(x: float):
#     return math.sin(x)

# def cosine(x: float):
#     return math.cos(X)

# def tangent(x: float):
#     return math.tan(x)

# def cotangent(x: float): 
#     return math.cos(x)

# def maximum(*args):
#     return max(*args)

# def minimum(*args):
#     return min(*args)

# def abstract(x: float):
#     return abs(x)

# def power(x: int, y:int):
#     return pow(x, y)

# def ceil(x: float):
#     return math.ceil(x)

# def floor(x: float):
#     return math.floor(x)

# def fact(x: int):
#     return math.factorial(x)

@client.event
async def on_ready():
    print(f"{client.user.name} is online...")
 

# ADD
@client.command()
async def add(ctx, x:float, y:float):
    res = addition(x ,y)
    return ctx.send(res)
# SUBTRACT
@client.command()
async def sub(ctx, x:float, y:float):
    res = subtract(x ,y)
    return ctx.send(res)
# DIVIDE
@client.command()
async def div(ctx, x:float, y:float):
    res = divide(x ,y)
    return ctx.send(res)
# RANDOM
@client.command()
async def random(ctx, x:int, y:int):
    res = random(x ,y)
    return ctx.send(res)
# SQUARE ROOT
@client.command()
async def sqrt(ctx, x:int, y:int):
    res = square(x)
    return ctx.send(res)
# # SINUS
# @client.command()
# async def sin(ctx, x:float):
#     res = sinus(x)
#     return ctx.send(res)
# # COSINUS
# @client.command()
# async def cos(ctx, x:float):
#     res = cosine(x ,y)
#     return ctx.send(res)
# # TANGENT
# @client.command()
# async def tan(ctx, x:float):
#     res = tangent(x ,y)
#     return ctx.send(res)
# # COTENGENT
# @client.command()
# async def cot(ctx, x:float):
#     res = cotangent(x ,y)
#     return ctx.send(res)
# # MINIMUM
# @client.command()
# async def min(ctx, *args):
#     res = minimum(*args)
#     return ctx.send(res)
# # MAXIMUM
# @client.command()
# async def max(ctx, *args):
#     res = maximum(*args)
#     return ctx.send(res)    
# # ABSTRACT
# @client.command()
# async def abs(ctx, x:float):
#     res = abstract(x ,y)
#     return ctx.send(res)
# # POWER
# @client.command()
# async def pow(ctx, x:int, y:int):
#     res = power(x ,y)
#     return ctx.send(res)
# # CEIL
# @client.command()
# async def ceil(ctx, x:float):
#     res = ceil(x ,y)
#     return ctx.send(res)
# # FLOOR 
# @client.command()
# async def floor(ctx, x:float):
#     res = flooe(x ,y)
#     return ctx.send(res)
# # FACTORIAL
# @client.command()
# async def fact(ctx, x:int):
#     res = fact(x ,y)
#     return ctx.send(res)


client.run(TOKEN)