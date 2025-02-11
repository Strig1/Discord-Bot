import discord
import random
import os
import re
import difflib
from discord.ext import commands

TOKEN = "Token"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

media_folder = "Folder Directory"
rare_media_folder = "Folder Directory"

# Ability to load quotes from a text file
def load_quotes(filename="quotes.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")


# Function to replace "@username" with actual Discord mentions
def load_quotes(filename="quotes.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

# Function to replace "@username" with actual Discord mentions
def replace_mentions(quote, guild):
    mention_pattern = r"@(\w+)"  # Captures only the first word after "@"

    # Create a dictionary of members {lowercased_name: member_object}
    member_map = {member.name.lower(): member for member in guild.members}
    nickname_map = {member.display_name.lower(): member for member in guild.members}

    def replace_match(match):
        username = match.group(1).strip().lower()  # Normalise case and remove spaces

        # Direct match (preferred)
        if username in member_map:
            return member_map[username].mention
        if username in nickname_map:
            return nickname_map[username].mention

        # Fuzzy match finds closest username
        all_names = list(member_map.keys()) + list(nickname_map.keys())
        closest_match = difflib.get_close_matches(username, all_names, n=1, cutoff=0.6)  # 60% similarity

        if closest_match:
            best_match = closest_match[0]
            member = member_map.get(best_match) or nickname_map.get(best_match)
            if member:
                return member.mention  # Replace with actual mention

        print(f"⚠️ Mention not found: {username}")  # Debugging log
        return match.group(0)  # Keep original text if no match found

    return re.sub(mention_pattern, replace_match, quote)

# Slash command for random quote
@bot.tree.command(name="quote", description="Get a random inspirational quote")
async def quote(interaction: discord.Interaction):
    quotes = load_quotes()  # Reloads quotes every time
    if not quotes:
        await interaction.response.send_message("No quotes available!", ephemeral=True)
        return

    random_quote = random.choice(quotes)
    formatted_quote = replace_mentions(random_quote, interaction.guild)
    await interaction.response.send_message(formatted_quote, allowed_mentions=discord.AllowedMentions(users=True))


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
