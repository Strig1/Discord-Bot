import discord
from discord.ext import commands
from datetime import timedelta
import re  # For regex matching

# Set up the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True  # Required for member timeout
bot = commands.Bot(command_prefix="!", intents=intents)

# User ID to target
restricted_user_id = "Target ID"

# Regex pattern to detect Tenor GIF links
TENOR_GIF_PATTERN = r"(https?:\/\/)?(www\.)?tenor\.com\/view\/\S+"

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}!")

@bot.event
async def on_message(message):
    # Ignore bot messages and messages from users who aren't the target
    if message.author.bot or message.author.id != restricted_user_id:
        return

    # Check if the message is in all caps (ignoring spaces and non-alphabetic characters)
    filtered_message = ''.join(filter(str.isalpha, message.content))
    if filtered_message.isupper() and len(filtered_message) > 0:
        # Delete the message
        await message.delete()

        # Time out the user for 30 seconds
        try:
            timeout_duration = timedelta(seconds=30)
            await message.author.timeout(timeout_duration)
        except discord.Forbidden:
            await message.channel.send("I do not have permission to timeout members.")

        # Warn the user in the same channel
        await message.channel.send(
            f"{message.author.mention}, please avoid typing in all caps. You have been timed out for 30 seconds."
        )
        return  # Stop further checks after timing out

    # Check if the message contains an attachment (e.g., image with specific file types)
    if any(attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) for attachment in message.attachments):
        # Delete the message
        await message.delete()

        # Time out the user for 30 seconds
        try:
            timeout_duration = timedelta(seconds=30)
            await message.author.timeout(timeout_duration)
        except discord.Forbidden:
            await message.channel.send("I do not have permission to timeout members.")

        # Warn the user in the same channel
        await message.channel.send(
            f"{message.author.mention}, you are not allowed to send images. You have been timed out for 30 seconds."
        )
        return  # Stop further checks after timing out

    # Check if the message contains a Tenor GIF link
    if re.search(TENOR_GIF_PATTERN, message.content):
        # Delete the message
        await message.delete()

        # Time out the user for 30 seconds
        try:
            timeout_duration = timedelta(seconds=30)
            await message.author.timeout(timeout_duration)
        except discord.Forbidden:
            await message.channel.send("I do not have permission to timeout members.")

        # Warn the user in the same channel
        await message.channel.send(
            f"{message.author.mention}, you are not allowed to send Tenor GIFs. You have been timed out for 30 seconds."
        )
        return  # Stop further checks after timing out

# Run the bot
bot.run("Token")