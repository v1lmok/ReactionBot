import discord
from discord.ext import commands
from colorama import Fore, Style

class Consts:
    def __init__(self):
        self.TOKEN = '111'
        self.ADD_CHANNEL_ID = 111
        self.REMOVE_CHANNEL_ID = 111
        self.LOGS_CHANNEL_ID = 111
        self.ROLE_ID = 111
        self.REACTION_ADD = '✅'
        self.REACTION_REMOVE = '🤡'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$ ', intents=intents)
consts = Consts()

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
    if payload.message_id == add_message.id and str(payload.emoji) == consts.REACTION_ADD:
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
