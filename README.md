# Pyhton Discord Bot


# Overview

This Discord bot was created using Python as a way to put my Python skills to use. It includes several features for moderation and general experimentation.


# Features

# 1. User Tracking

* Originally designed to track a specific user who would join and leave multiple times a day.

* The bot logs each join and leave event in a separate JSON file.

* It tracks how many times a user joins and leaves within a 24-hour period (resetting at midnight UK time).

* Users can check these stats using the !check command.

# 2. Moderation

* Prevents users from typing in all caps.

  * Blocks users from sending GIFs and images.

  * Issues warnings and times out users for 30 seconds if they violate these rules.

# 3. Slash Commands

* /media: Randomly posts a GIF, image, or video from a specified directory.

* /quote: Selects a random quote from a predefined Python dictionary and posts it.


# Prerequisites

* Python 3.8 or higher.

* Required Python libraries (can be installed via requirements.txt).



# Usage

# Commands

# Prefix Commands:

  * !check: View the stats for user join/rejoin activity.

# Slash Commands:

  * /media: Posts a random media file (gif, image, or video).

  * /quote: Posts a random quote.

# Moderation Features

* Automatically monitors and enforces rules for:

  * Excessive use of caps.

  * Posting unauthorized gifs or images.



# Customisation

You can extend the bot's functionality by modifying the Python files:

* User Tracking: Edit the logic in the tracking module to adjust behaviour.

* Media and Quotes: Update the directories or dictionary for the /media and /quote commands.

* Moderation: Modify rules or add new ones in the moderation module.



# Contributing

If you'd like to contribute:

 1. Fork the repository.

 2. Create a new branch.

 3. Make your changes and submit a pull request.



# License

This project is licensed under the MIT License.

# Acknowledgements

This bot was created as a way to explore Python and Discord bot development. Special thanks to the Discord.py library and the open-source community for inspiration and support.































