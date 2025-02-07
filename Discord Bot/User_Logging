import discord
from discord.ext import commands, tasks
from datetime import datetime
import json
import os
import pytz  # Library for timezone handling
import asyncio

# Bot setup
TOKEN = 'Token'

# Set Discord user you want to monitor
TARGET_USER_ID = "Target ID"

DATA_FILE = "user_activity.json"
UK_TZ = pytz.timezone("Europe/London")  # Set timezone

# Function to load existing data from file (Creates file if missing)
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        print("No existing data file found. Creating a new one...")
        return {'total_joins': 0, 'total_leaves': 0, 'joins': [], 'leaves': []}  # Default values

# Function to save data back to file
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(user_activity_data, file, indent=4)  # Pretty JSON formatting
    print("Data saved successfully.")

# Load user data AFTER defining the functions
user_activity_data = load_data()
save_data()  # Ensure the file is created when bot starts

# Initialize bot with intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Reset at midnight UK time
@tasks.loop(minutes=1)  # Runs every minute to check the time
async def reset_daily_counts():
    now_uk = datetime.now(UK_TZ)  # Get current UK time
    if now_uk.hour == 0 and now_uk.minute == 0:  # Midnight UK time
        user_activity_data['joins'] = []
        user_activity_data['leaves'] = []
        save_data()
        print("Daily reset completed at midnight UK time.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    print("Bot is running and ready.")
    reset_daily_counts.start()  # Start the UK time midnight reset loop

@bot.event
async def on_member_join(member):
    if member.id == TARGET_USER_ID:
        user_activity_data['total_joins'] += 1
        user_activity_data['joins'].append(datetime.utcnow().isoformat())
        save_data()  # Save updated data
        print(f"{member.name} joined. Total joins: {user_activity_data['total_joins']}")

@bot.event
async def on_member_remove(member):
    if member.id == TARGET_USER_ID:
        user_activity_data['total_leaves'] += 1
        user_activity_data['leaves'].append(datetime.utcnow().isoformat())
        save_data()  # Save updated data
        print(f"{member.name} left. Total leaves: {user_activity_data['total_leaves']}")

@bot.command(name='check')
async def check_count(ctx):
    await ctx.send(
        f"User has joined a total of {user_activity_data['total_joins']} times and left a total of {user_activity_data['total_leaves']} times.\n"
        f"In the last 24 hours (reset at midnight UK time), they have joined {len(user_activity_data['joins'])} times and left {len(user_activity_data['leaves'])} times."
    )

bot.run(TOKEN)
