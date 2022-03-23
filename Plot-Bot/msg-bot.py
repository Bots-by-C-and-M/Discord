'''
This bot pulls daily message history from specified channels
and returns a summary of key information to the moderators of
the Discord server.

Structure
1.  Imports
2.  Connections
3.  Variables
4.  Functions
5.  Callbacks
'''

# 1. Imports
# Libraries & Functionality
import os, asyncio, discord
import requests, json
import random, time
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

# Local
# from modeling import clean_data

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 2. Connections
# Env File
load_dotenv()

# Discord
TOKEN = os.getenv('MSG_SUMMARY_BOT')
client = discord.Client()
embed = discord.Embed()

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 3. Variables
# For testing
test_msg = 'This is a test of the reply function'

# Message Replies
help_info = '''
--------------------------------------------
                Commands
--------------------------------------------

`$activate` to receive a full summary at 24
            hour intervals at Midnight
            Pacific Standard Time

`$deactivate` to disable automatic summaries

`$full` to receive a full summary

`$key` to receive top 20 used words

`$topics` to receive topics of discussion

--------------------------------------------
--------------------------------------------
'''

activate_msg = '''
Automatic summaries will be sent to this channel "message-summaries" every 24 hours at Midnight Pacific Standard Time.
'''

deactivate_msg = 'Automatic Summaries have been disabled. Enter `$activate` to enable them again.'

# 4. Functions

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

# 5.Callbacks
# On Bot connection
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

# On Bot Addition/Removal to Guild
@client.event
async def on_guild_join(guild):
    print('Message Summary Bot has joined.')

@client.event
async def on_guild_remove(guild):
    print('Message Sumary Bot has been removed.')

# On Message
@client.event
async def on_message(message):
    # Return nothing for messages from this bot
    if message.author == client.user:
        return

    # Check Command has come from **MOD ONLY** (Done manually by server mods)
    # Channel called "message-summaries"
    if message.channel.name == 'message-summaries':

        # HELP
        if message.content.startswith('$help'):
            await message.channel.send(help_info)

        # Automatic Summaries
        # Off
        if message.content.startswith('$activate'):
            await message.channel.send(activate_msg)

            while 1 == True:
                await asyncio.sleep(86400)

                # On
                if message.content.startswith('$deactivate'):
                    await message.channel.send(deactivate_msg)
                    break

        # Return Summaries
        # Full Summary
        if message.content.startswith('$full'):
            await message.channel.send(test_msg)

        # Key Words Only
        if message.content.startswith('$key'):
            await message.channel.send(test_msg)

        # Sentiments Only
        if message.content.startswith('$sentiment'):
            await message.channel.send(test_msg)

        # Topics Only
        if message.content.startswith('$topics'):
            await message.channel.send(test_msg)

        # Testing
        if message.content.startswith('$test'):

            test_df = sns.load_dataset("tips")
            test_plt = sns.barplot(x="tip", y="day", data=test_df)

            fig = test_plt.figure
            fig.savefig('plots/test_plot.png', dpi=300)

            with open('plots/test_plot.png', 'rb') as f:
                file = io.BytesIO(f.read())

            test_image = discord.File(
                file, filename='test_plot.png'
                )

            test_embed = discord.Embed(
                title="This is a Test",
                description="To see if my images embed locally",
                )

            embed.set_image(url="attachment://test_plot.png")

            await message.channel.send(test_msg)
            await message.channel.send(file=test_image, embed=test_embed)

# #### # #### # #### # #### # #### # #### # #### # #### # #### # #### # #### #

client.run(TOKEN)
