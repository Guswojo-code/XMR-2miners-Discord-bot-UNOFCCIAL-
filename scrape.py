import requests
import json
import discord
from discord import *
from discord.ext import commands
from time import sleep
from dotenv import load_dotenv
import datetime

intents = discord.Intents.all()
date = datetime.datetime.now()





def update():
    url = "https://xmr.2miners.com/api/accounts/" + acc
    response = requests.get(url)
    if response.status_code != 200:
        print('error {}'.format(response.status_code))
    else:
        data = json.loads(response.text)
        current_hashrate = data["currentHashrate"]
        print("Updated!")



#Discord bot:


load_dotenv()

bot = commands.Bot(command_prefix='!', intents=intents)
token  = 'MTAyODMxNDk2NjgzMjQ0NzU4OA.GiWN4z.a3Fi_QdU6GVPZowkqN-Upe20KKd8vbkUSnckJY'

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def info(ctx, args1):
    #Update the data
    acc = args1
    url = "https://xmr.2miners.com/api/accounts/" + acc
    response = requests.get(url)
    data = json.loads(response.text)
    current_hashrate = data["currentHashrate"]
    avr_hashrate = data["hashrate"]
    workersOnline = data["workersOnline"]
    workersOffline = data["workersOffline"]
    workers = data["workersTotal"]
    #print(json.dumps(data, indent=4))
    
    #Send the results:
    await ctx.message.delete()
    embed=discord.Embed(title="Current hashrate: " + str(current_hashrate) + "\n Average hashrate: " + str(avr_hashrate) + "\n Workers online: " + str(workersOnline) + " / " + str(workers), color=0xFF5733)
    embed.set_thumbnail(url='https://www.getmonero.org/press-kit/symbols/monero-symbol-on-white-480.png')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


bot.run(token)

    

