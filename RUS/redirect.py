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
    print(f'{Fore.CYAN}Бот вошёл как {Style.RESET_ALL}{bot.user}')

@bot.command()
async def send(ctx, channel_id: int, message: str, *, anon: bool):
    channel = bot.get_channel(channel_id)
    try:
        print(f'{Fore.GREEN}Получена команда отправки от {ctx.author}{Style.RESET_ALL} ({ctx.author.id}){Fore.GREEN} в канал {Style.RESET_ALL}{channel} ({channel_id}){Fore.GREEN} с сообщением: {Style.RESET_ALL}"{message}"')
        if channel is not None and not anon:
            await channel.send(f'@{ctx.author}: {message}')
            await ctx.send(f'Сообщение отправлено в канал {channel} ({channel_id}) с анонимностью: {anon}')
            print(f'{Fore.GREEN}{ctx.author}{Style.RESET_ALL} ({ctx.author.id}){Fore.GREEN} успешно отправил сообщение {Style.RESET_ALL}"{message}"{Fore.GREEN} в {channel} ({channel_id}) с анонимностью: {Style.RESET_ALL}{anon}')
        elif channel is not None:
            await channel.send(f'@Anonymous: {message}')
            await ctx.send(f'Сообщение отправлено в канал {channel} ({channel_id}) с анонимностью: {anon}')
            print(f'{Fore.GREEN}{ctx.author}{Style.RESET_ALL} ({ctx.author.id}){Fore.GREEN} успешно отправил сообщение {Style.RESET_ALL}"{message}"{Fore.GREEN} в {channel} ({channel_id}) с анонимностью: {Style.RESET_ALL}{anon}')
        else:
            await ctx.send(f'Канал с ID {channel_id} не найден')
            print(f'{Fore.RED}{ctx.author} {Style.RESET_ALL}({ctx.author.id}){Fore.RED} указал неверный ID канала {Style.RESET_ALL}({channel_id})')
            time.sleep(0.8)
            print(f'{Fore.RED}Отменено для {ctx.author}{Style.RESET_ALL} ({ctx.author.id})')
    except Exception as e:
        logging.error(f'Произошла ошибка: {e}')
        await ctx.send(f'Произошла ошибка: {e}')

@bot.command()
async def helps(ctx, *, arg: str = None):
    if arg is not None:
        if arg == 'redir':
            await ctx.send(f'channel_id: int, message: str, anon: bool\nПример: $ send 1241453802541023343 "Привет, мир!" True')
        elif arg == 'react':
            await ctx.send(f'Поставьте реакцию, чтобы получить роль, или удалите реакцию, чтобы убрать роль')
    else:
        await ctx.send(f'$ helps redir\n$ helps react')

bot.run(consts.TOKEN)
