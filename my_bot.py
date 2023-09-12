import discord
import requests
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

# file with your token api 
# first line is api discord
# two line is api steam
file_token = open('env.txt', 'r')
Lines = file_token.readlines()
api_keys = [] 

count = 0
# Read line by line
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    api_keys.append(line.strip())

class MyClient(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        print(f'Message from {message.author}: {message.content}')
        await message.channel.send(f'Hello {message.author}!')
        await self.process_commands(message)



@commands.command()
async def test(ctx):
    await ctx.send("test")
    
@commands.command()
async def send_msg(ctx, arg):
    await ctx.send(arg)

@commands.command()
async def getgames(ctx):
    all_games = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json')
    print("amount games :",len(all_games.json()))
    print(all_games.json())

cli = MyClient(command_prefix='/', intents=intents)
cli.add_command(test)
cli.add_command(send_msg)
cli.add_command(getgames)
cli.run(api_keys[0])