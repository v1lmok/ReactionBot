import logging
import discord
import time
from discord.ext import commands
from colorama import Fore, Style

class Consts:

    def __init__(self):
        self.TOKEN = '111'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$ ', intents=intents)
logging.basicConfig(level=logging.INFO)
consts = Consts()

@bot.event
async def on_ready():
    print(f'{Fore.CYAN}Bot has logged in as {Style.RESET_ALL}{bot.user}')

@bot.command()
async def send(ctx, channel_id: int, message: str, *, anon: bool):
    channel = bot.get_channel(channel_id)
    try:
        print(f'{Fore.GREEN}Received send command from {ctx.author}{Style.RESET_ALL} ({ctx.author.id}){Fore.GREEN} to channel {channel} {Style.RESET_ALL}({channel_id}){Fore.GREEN} with message: {Style.RESET_ALL}"{message}"')
        if channel is not None and not anon:
            await channel.send(f'@{ctx.author}: {message}')
            await ctx.send(f'Message sent to channel {channel} ({channel_id}) with anon: {anon}')
            print(f'{Fore.GREEN}{ctx.author}{Style.RESET_ALL} ({ctx.author.id}){Fore.GREEN} successfully sent message {Style.RESET_ALL}"{message}"{Fore.GREEN} to {channel} {Style.RESET_ALL}({channel_id}){Fore.GREEN} with anon: {Style.RESET_ALL}{anon}')
        elif channel is not None:
            await channel.send(f'@Anonymous: {message}')
            await ctx.send(f'Message sent to channel {channel} ({channel_id}) with anon: {anon}')
            print(f'{Fore.GREEN}{ctx.author}{Style.RESET_ALL} ({ctx.author.id}){Fore.GREEN} successfully sent message {Style.RESET_ALL}"{message}"{Fore.GREEN} to {channel} {Style.RESET_ALL}({channel_id}){Fore.GREEN} with anon: {Style.RESET_ALL}{anon}')
        else:
            await ctx.send(f'Channel with ID {channel_id} not found')
            print(f'{Fore.RED}{ctx.author} {Style.RESET_ALL}({ctx.author.id}){Fore.RED} pointed to the wrong channel ID {Style.RESET_ALL}({channel_id})')
            time.sleep(0.8)
            print(f'{Fore.RED}Aborted for {ctx.author}{Style.RESET_ALL} ({ctx.author.id})')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        await ctx.send(f'An error occurred: {e}')

@bot.command()
async def helps(ctx, *, arg: str = None):
    if arg is not None:
        if arg == 'redir':
            await ctx.send(f'channel_id: int, message: str, anon: bool\nExample: $ send 1241453802541023343 "Привет, мир!" True')
        elif arg == 'react':
            await ctx.send(f'Put reaction to get role or remove reaction to remove role')
    else:
        await ctx.send(f'$ helps redir\n$ helps react')


bot.run(consts.TOKEN)
