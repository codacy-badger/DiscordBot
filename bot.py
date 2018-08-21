#Lif3 Bot by ItzAfroBoy

#Setup
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

#Prefix
bot = commands.Bot(command_prefix='#')
bot.remove_command('help')

token = "BOT TOKEN"

#Launching Messgae
print("")
print("Launching Lif3 Bot ...")
print("----------------------")
print("")

#Events


@bot.event
async def on_ready():
#    await bot.change_presence(game=discord.Game(name='STATUS'))
    print("Bot Version: 1.0.1")
    time.sleep(1)
    print("Discord Version: " + discord.__version__)
    time.sleep(0.9)
    print(bot.user.name + " Online")
    print("-----------------------")
    print("")


# @bot.event
# async def on_member_join(ctx):
#     author = ctx.message.author
#     await bot.send_message(author, 'Welcome to {}'.format(ctx.message.server))
#     time.sleep(2)
#     await bot.send_message(author, 'Please react for a role in [CHANNEL]')
#     await bot.send_message(author, 'Type #help for a list of available')

#Commands


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!! xSSS")
    print("{} has pinged".format(ctx.message.author))


@bot.command(pass_context=True)
async def pong(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print("{} has ponged".format(ctx.message.author))


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I've got", color=0x00ff00)
#    embed.set_author(name="[Your Name]")
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest Role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print("{} has requested {}'s Info".format(ctx.messsage.author, user.name))


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{} info".format(ctx.message.server.name), description="Here's what I've got", color=0x00ff00)
#    embed.set_author(name="[Your Name]")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print("{} has requested {} Info".format(ctx.message.author, ctx.message.server.name))


@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Commands", description="Here's all the commands avaliable", color=0x00ff00)
#    embed.set_author(name="[Your Name]")
    embed.add_field(name='#ping', value='pong', inline=True)
    embed.add_field(name='#pong', value='ping', inline=True)
    embed.add_field(name='#info [@Username]',value='Get info about a member', inline=True)
    embed.add_field(name='#serverinfo',value='Get info about the server', inline=True)
    embed.add_field(name='#help', value='Show this menu', inline=True)
    embed.add_field(name='#clear', value='Clear all messages', inline=True)
    embed.add_field(name='#restart', value='Restart the bot', inline=True)
    embed.add_field(name='#suicide', value='Change the bot presence to a suicide related comment', inline=True)
    embed.add_field(name='#lonely', value='When you feel lonely', inline=True)
    embed.add_field(name='#kick [@username]', value='Kicks someone', inline=True)
    await bot.say(embed=embed)
    print("{} needs help".format(ctx.message.author))


@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say('{} Messages Deleted'.format(amount))
    print("{} Messages have been deleted in {}".format(amount, ctx.message.channel))


@bot.command(pass_context=True)
async def restart(ctx):
    print("Bot Restarting")
    bot.logout
    time.sleep(30)
    await bot.login(token)
    print("Bot restarted")
    print("-------------")


@bot.command(pass_context=True)
async def suicide(ctx):
    await bot.change_presence(game=None)
    time.sleep(1.5)
    await bot.change_presence(game=discord.Game(name='Suicide is next'))
    print("{} changed my presence".format(ctx.message.author))


@bot.command(pass_context=True)
async def lonely(ctx):
    author = ctx.message.author
    await bot.send_message(author, 'Get some friends then')
    print("{} is lonely".format(ctx.message.author))


@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

bot.run(token)
