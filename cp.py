import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')
    print('------')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Wesh {interaction.user.mention} !!!")

@bot.tree.command(name="poke")
@app_commands.describe(thing_to_say = "je ping qui ?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"hé oh {thing_to_say}")

    
# Démarrer le bot
bot.run('MTExMjEzMDI4MzMyMDM5Mzg3OQ.Gp694g.12LCh9prHkpWFNduU5WDw9zC8QGOFskkLEGCHI')  # Remplacez 'TOKEN' par votre jeton d'identification Discord
