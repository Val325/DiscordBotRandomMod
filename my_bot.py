import discord
import requests
from discord import app_commands 

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

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync() #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'get_games', description='get amount games from steam api') #guild specific slash command
async def slash2(interaction: discord.Interaction):
    all_games = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v0002/?format=json')
    print("amount games :",len(all_games.json()["applist"]["apps"]))
    amount_games = "get amount " + str(len(all_games.json()["applist"]["apps"]))
    await interaction.response.send_message(amount_games, ephemeral = True) 

client.run(api_keys[0])