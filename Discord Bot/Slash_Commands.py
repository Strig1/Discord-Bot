import discord
import random
import os
from discord.ext import commands

TOKEN = "Token"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

media_folder = "Folder Directory"
rare_media_folder = "Folder Directory"

quotes = [
    "quote 1",
    "Quote 2",

]
# Randomly selects a quote from the list
@bot.tree.command(name="quote", description="Get a random inspirational quote")
async def quote(interaction: discord.Interaction):
    random_quote = random.choice(quotes)
    await interaction.response.send_message(random_quote)


# Randomly selects a quote from the list
@bot.tree.command(name="quote", description="Get a random inspirational quote")
async def quote(interaction: discord.Interaction):
    random_quote = random.choice(quotes)
    await interaction.response.send_message(random_quote)


# Slash command:
@bot.tree.command(name="media", description="Get a random image, gif, or video!")
async def media(interaction: discord.Interaction):
    await interaction.response.defer()  # This prevents Discord from invalidating the interaction

    # Roll a random number and print it
    random_number = random.randint(1, 1_000_000)
    print(f"Rolled number: {random_number}")

    # Placeholder: always selects media_folder
    chosen_folder = rare_media_folder if random_number == 1 else media_folder  # Uncomment to enable rarity check
    # List all media files
    media_files = [f for f in os.listdir(media_folder) if f.endswith(('.jpg', '.png', '.gif', '.mp4'))]

    if not media_files:  # Handle empty folder case
        await interaction.response.send_message("No media files found!", ephemeral=True)
        return

    # Choose a random media file
    random_media = random.choice(media_files)
    file_path = os.path.join(media_folder, random_media)

    try:
        with open(file_path, "rb") as file:
            await interaction.followup.send(file=discord.File(file, filename=random_media))  # Use followup.send()
    except discord.errors.HTTPException as e:
        if e.code == 40005:  # File too large
            await interaction.followup.send("File is too large to send!", ephemeral=True)
        else:
            await interaction.followup.send("An error occurred while sending the file.", ephemeral=True)
    except Exception as e:
        print(f"Error: {e}")
        await interaction.followup.send("An unexpected error occurred!", ephemeral=True)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot is ready as {bot.user}")

bot.run(TOKEN)
