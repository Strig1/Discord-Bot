# Python Discord Bot


# Overview

This Discord bot was created using Python as a way to put my Python skills to use. It includes several features for moderation and general experimentation.


# Features

# 1. User Tracking

* !check: View the stats for user join/rejoin activity.
  
* Originally designed to track a specific user who would join and leave multiple times a day.

* The bot logs each join and leave event in a separate JSON file.

* It tracks how many times a user joins and leaves within a 24-hour period (resetting at midnight UK time).

* Users can check these stats using the !check command.
 
   
 
# 2. Moderation Features

* Automatically monitors and enforces rules for:

  * Prevents user from using all caps.

  * Blocks user from sending GIFs and images.

  * Issues warnings and times out user for 30 seconds if they violate these rules.
 
     
 
# 3. Slash Commands

* /media: Randomly posts a GIF, image, or video from a specified directory with the ability to add rarity drop rate.

* /quote: Selects a random quote from a predefined Python dictionary and posts it.
 
 
 
 
 
# Prerequisites

* Python 3.8 or higher.

* Required Python libraries: pip install discord.py pytz



































