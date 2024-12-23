import discord
from discord.ext import commands

# Set up intents to allow reading messages
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {bot.latency * 1000:.2f}ms')

# Use your actual bot token here
bot.run('MTI4ODE1OTA3ODUyNjQ4ODYyNg.GPIPeo.7exD4mdrp2HARWvt_lBKQqbP7fzwPPwZt-KStI')
