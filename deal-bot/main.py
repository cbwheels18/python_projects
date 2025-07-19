import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

liter67 = "https://cars.ksl.com/search/make/Dodge;Nissan;Ram/mileageTo/1000000/priceTo/20000/body/Truck/transmission/Automatic/liters/6.7L/fuel/Diesel"
liter59 = "https://cars.ksl.com/search/make/Dodge;Nissan;Ram/mileageTo/1000000/priceTo/20000/body/Truck/transmission/Automatic/liters/5.9L/fuel/Diesel"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!hello'):
        await message.channel.send('Hello')

    if message.content.lower().startswith('!car'):
        await message.channel.send('make, model, mileage')

    if message.content.lower().startswith('!ksl'):
        await message.channel.send('cars.ksl.com')

    if message.content.lower().startswith('!search'):
        user_input = message.content[8:].strip()  # Remove the !search and leading/trailing spaces
        parts = user_input.split()

        if len(parts) == 5:
            make, mileage, price, transmission, fuel = [part.capitalize() for part in parts]
            link = f"https://cars.ksl.com/search/make/{make}/mileageTo/{mileage}/priceTo/{price}/transmission/{transmission}/fuel/{fuel}"
            await message.channel.send(link)
        else:
            await message.channel.send('Please provide all five parameters (make, mileage, price, transmission, fuel) separated by spaces.')

client.run(TOKEN)
