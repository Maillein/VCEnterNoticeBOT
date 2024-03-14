import os
import discord
from dotenv import load_dotenv

intents=discord.Intents.default()
client = discord.Client(intents=intents)

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
NOTICE_CHANNEL_ID = int(os.getenv('NOTICE_CHANNEL_ID'))

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        notice_channel = client.get_channel(NOTICE_CHANNEL_ID)
        if after.channel is not None:
            msg = f'{member.name}が{after.channel.name}に参加しました'
            await notice_channel.send(msg)
        if before.channel is not None:
            msg = f'{member.name}が{before.channel.name}から退出しました'
            await notice_channel.send(msg)

client.run(DISCORD_TOKEN)
