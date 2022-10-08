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

#Discord part

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=intents)
token  = 'TOKEN'

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
    
    #Math
    if current_hashrate > 1000000:
        current_units = " MH/s"
        current_hashrate = current_hashrate/1000000

    elif current_hashrate > 1000:
        current_units = " KH/s"
        current_hashrate = current_hashrate/1000
    else:
        current_units = " H/s"

    if avr_hashrate > 1000000:
        avr_units = " MH/s"
        avr_hashrate = avr_hashrate/1000000

    elif avr_hashrate > 1000:
        avr_units = " KH/s"
        avr_hashrate = avr_hashrate/1000
    else:
        avr_units = " H/s"
   
    #Format the numbers so they look *Beautiful*

    current_hashrate_formatted = "{:.2f}".format(current_hashrate)
    avr_hashrate_formatted = "{:.2f}".format(avr_hashrate)


    #Send the results:
    await ctx.message.delete()
    embed = discord.Embed(title="Current hashrate: " + str(current_hashrate_formatted) + current_units + "\n Average hashrate: " + str(avr_hashrate_formatted) + avr_units + "\n Workers online: " + str(workersOnline) + " / " + str(workers), color=0xFF5733)
    embed.set_thumbnail(url='https://www.getmonero.org/press-kit/symbols/monero-symbol-on-white-480.png')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)


bot.run(token)

    

