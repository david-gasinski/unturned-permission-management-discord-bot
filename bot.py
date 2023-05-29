# This file servers as the basis of the bot. 
# Here the bot is ran and all the commands are loaded

# Imports
from discord.ext import commands
from dotenv import load_dotenv
import os
import discord
import requests
import datetime

# Load .env 
load_dotenv()

# Setup initial variables
intents = discord.Intents.default()
intents.message_content = True

# Discord bot token
TOKEN = os.getenv('TOKEN')

# Channel ID where commands and replies are sent
channel_id = int(os.getenv('COMMAND_CHANNEL_ID')) 

# Bot prefix
bot = commands.Bot(command_prefix='$', intents=intents)

# URL 
URL = os.getenv('URL')
LOG_DIR=os.getenv('LOG_DIR')

# Method which sends a POST request to the given URL with data
def sendRequest(steamid, perm, endpoint):
    # Send the request
    response = requests.post(f'{URL}/{endpoint}', json={'steamid': steamid, 'permission': perm})
    # Return the response
    return response.json()

# CONVERTS TO A DISCORD EMBED
def convertEmbed(text):
    return discord.Embed(description=text)

# LOGS THE COMMAND IN THE COMMANDS_RAN FILE
def logCommand(ctx, command, success):
    with open (LOG_DIR, 'a') as f:
        f.write(f'\n Command {command} ran by {ctx.author} / {ctx.author.name} at {datetime.datetime.now()}. It was ran successfully: {success}.')
        f.close()
        
# Setting commands and blacklisted roles
blacklisted = ['owner', 'headadmin','admin', 'moderator', 'developer']
commands_with_permissions = ['add', 'remove']

# Setting up the bot commands
# Bot has one command but with multiple subcommands
@bot.command()
async def perms(ctx, command, *args):
    # do nothing if not in the correct channel
    command = command.lower()
    steamid = args[0]
    permissions = args[1:]
    success = 0
    success_criteria = len(permissions)
    channel = bot.get_channel(channel_id)
    
    if ctx.channel.id != channel_id:
        return
    
    if command in commands_with_permissions:
        if len(args) == 0:
            await channel.send('Please specify a permission.')
            return
    
        for perm in permissions:
            if perm in blacklisted:
                await channel.send(f'*{perm}* is a **restricted** permission.')
                logCommand(ctx, command, False)
            else:
                response = sendRequest(steamid, perm.lower(), command)
                logCommand(ctx, command, response['status'])
                if (response['status']):
                    success += 1
                
        if success == success_criteria:
            if success == 1:
                await channel.send(f'The operation **{command}** has been successful on {success} permission.')
            else:
                await channel.send(f'The operation **{command}** has been successful on {success} permissions.')
        else:
            if (success_criteria - success) == 1:
                await channel.send(f'Failed to {command} {success_criteria - success} permission. Please check the spelling of the permission, or verify that the steamid provided is correct.')
            else: 
                await channel.send(f'Failed to {command} {success_criteria - success} permissions. Please check the spelling of the permissions, or verify that the steamid provided is correct.')
    elif command == 'view':
        response = sendRequest(steamid, None, command)
        markdown_response = f'The steamid *{steamid}* has the following permissions:'
        
        for perm in response['message']:
            markdown_response += f'\n > {perm}'
        
        logCommand(ctx, command, True)
        await channel.send(markdown_response)
    elif command == 'check':
        response = sendRequest(steamid, perm, command)
        if response['status']:
            logCommand(ctx, command, True)
            await channel.send(f'The steamid *{steamid}* has the permission *{perm}*.')
        else:
            logCommand(ctx, command, True)
            await channel.send(f'The steamid *{steamid}* does not have the permission *{perm}*.')
        

# HELP CLASS

class CustomHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
            channel = bot.get_channel(channel_id)
            if self.context.channel.id != channel_id:
                return
            help_text = """
                            ```Commands:
            > $perms add [steamid] [permissions]
            you can add multiple permissions to one steamid. Example:
                "?perms add 0778312777312736 god demi hecate"
                This will add God, Demi and Hecate to the steamid 0778312777312736.

            > $perms remove [steamid] [permissions]
            you can remove multiple permissions from a steamid. Example:
                "?perms remove 0778312777312736 god demi hecate"
                This will remove God, Demi, Hecate from the steamid 0778312777312736

            > $perms view [steamid]
            allows you to view the permissions of a given steamid. Example:
                "?perms view 0778312777312736"

            > $perms check [steamid] [permission]
            allows you to check if a steamid has a given permission. This only works for one permission at a time. Example:
                "?perms check 0778312777312736 hecate"
            ```       
            """
            await channel.send(help_text)     

# Run the bot
bot.help_command = CustomHelp()
bot.run(TOKEN)