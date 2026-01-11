import discord
import os  # allows us to read the token safely

TOKEN = os.getenv("put t here")  # Render will store your token securely
ROBLOX_GAME = "https://www.roblox.com/games/123456789/YOURGAME"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_guild_join(guild):
    channel = guild.system_channel
    message = f"🎮 Thanks for inviting me!\nPlay the game here:\n{ROBLOX_GAME}"

    if channel and channel.permissions_for(guild.me).send_messages:
        await channel.send(message)
        return

    for ch in guild.text_channels:
        if ch.permissions_for(guild.me).send_messages:
            await ch.send(message)
            break

client.run(TOKEN)
