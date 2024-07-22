import discord
from openai import AsyncOpenAI
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True

# Mengambil token dan API key dari environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = discord.Client(intents=intents)
openai_client = AsyncOpenAI(api_key=openai_api_key)

async def ask_gpt(message_content):
    try:
        response = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": message_content
                }
            ]
        )
        answer = response.choices[0].message.content
        return answer
    except Exception:
        return "bayar dulu geh VIP, bot ga jalan ini kalo gratisan mah udah limit brader"

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "test":
        await message.channel.send("ya apa coy ?, aman nih gw")
    elif message.content.lower() == "good":
        await message.channel.send("yoii, ketik aja prompt nya")
    elif message.content.lower().startswith("/bot"):
        query = message.content[len("/bot "):] # Menghapus awalan /bot dan mengambil isi pesannya
        response = await ask_gpt(query)
        await message.channel.send(response)

client.run(DISCORD_TOKEN)
