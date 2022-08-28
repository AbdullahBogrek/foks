import discord
from discord.ext import commands    

class Mod(commands.Cog):
    def __init__ (self, client):
        self.client = client
        self.activities = {}

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("hi")

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def clear(self, ctx, line = 1):
        await ctx.channel.purge(limit = line)
        admin = ctx.author
        print(f"{line} lines have been deleted by the {admin} .")
   
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *args, reason = "Pepega"):
        await member.kick(reason = reason)
        admin = ctx.author
        print(f"{member} is kicked the channel by the {admin}.")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *args, reason = "Pepega"):
        await member.ban(reason = reason)
        admin = ctx.author
        print(f"{member} is banned the channel by the {admin}.")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for bans in banned_user:
            user = bans.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned user {user.mention}")
                return

        admin = ctx.author
        print(f"The ban of {member} user has been removed by the {admin}.")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def mute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(833793972731117639)
        await member.add_roles(muted_role)
        await ctx.send(member.mention + " has been muted.")
        print(f"{member} has been muted.")

    @commands.command()
    async def status(self, ctx, activity, *, state):
        self.change_status(state)
        await self.client.change_presence(**self.activities.get(activity))
    # The python will execute according to the parameter length.
    @commands.command()
    async def status(self, ctx, activity, url, *, state):
        self.change_status(state, url)
        await self.client.change_presence(**self.activities.get(activity))

    def change_status(self, state, url = ''):
        self.activities = {
            "game" : {"activity": discord.Game(name = state)},
            "listening" : {"activity": discord.Activity(type = discord.ActivityType.listening, name = state)},
            "watching" : {"activity": discord.Activity(type = discord.ActivityType.watching, name = state)},
            "streaming" : {"activity": discord.Streaming(name = state, url = url)},
        }

# This functions is special for cogs. 
def setup(client):
    client.add_cog(Mod(client))
