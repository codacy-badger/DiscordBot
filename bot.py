# Bot by ItzAfroBoy

# Setup
import discord
from discord.ext import commands
from discord.ext.commands import bot
import time
import asyncio

# Prefix
bot = commands.Bot(command_prefix='~')
bot.remove_command('help')

token = ""

# Launching
print()
print("Starting your Bot...")
print("--------------------")
print()


# Events
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='With ItzAfroBoy'))
    print("Version: 1.0.0")
    time.sleep(1)
    print("Discord Version: " + discord.__version__)
    time.sleep(1)
    print(bot.user.name + " Online")
    print("-----------------------")
    print()

# Commands


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="Help", description="Here are commands you can use.", color=0xBF590E)
    embed.add_field(name="Ping", value="Find out :smiling_imp:", inline=False)
    embed.add_field(name="Clear", value="Clear's messages in a channel. \nPlease note, maximum is 100 messages and the bot will display the number\nthat you want deleted.")
    embed.add_field(name="Help", value="Shows this menu")
    await bot.send_message(author, embed=embed)


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Someone pinged?? :confused:")
    print("{} pinged".format(ctx.message.author))


@bot.command(pass_context=True)
async def clear(ctx, number):
    mgs = []
    number = int(number)
    async for i in bot.logs_from(ctx.message.channel, limit=number):
        mgs.append(i)
    await bot.delete_messages(mgs)
    message = await bot.say("`{}` messages deleted".format(number))
    print("I have deleted {} messages. {} wanted them deleted".format(number, ctx.message.author))
    time.sleep(1)
    await bot.delete_message(message)

bot.run(token)
