import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())
# bot = commands.Bot(command_prefix='/')
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command()
async def hello(message):
    await message.channel.send('Hi!')
    bot.process_commands(message)
 
bot.run('@bot_token')