#VERSION 2.0

import discord
import sqlite3
from dotenv import load_dotenv
import os
from db_interact import *

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    dbInit()

    print('Bot Online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == 'mug':
        if "mug" in message.content and len(message.content) == 3:
            rows = getRows(message.author.id)
            mugs = getMugs(message.author.id)
            if len(rows) == 0:
                initUserMugs(message.author.id)
            else:
                addMugs(message.author.id)
                if mugs[0] >= 25:
                    await message.author.add_roles(discord.utils.get(message.guild.roles, name="25+ Mugs"))
                if mugs[0] >= 100:
                    await message.author.add_roles(discord.utils.get(message.guild.roles, name="100+ Mugs"))
                if mugs[0] >= 250:
                    await message.author.add_roles(discord.utils.get(message.guild.roles, name="250+ Mugs"))
                if mugs[0] >= 500:
                    await message.author.add_roles(discord.utils.get(message.guild.roles, name="500+ Mugs"))
                if mugs[0] >= 1000:
                    await message.author.add_roles(discord.utils.get(message.guild.roles, name="1000+ Mugs"))
        else:
            rows = getRows(message.author.id)
            if len(rows) == 0:
                initUserJail(message.author.id)
            else:
                jailUser(message.author.id)
            jailed = getJailed(message.author.id)
            if jailed[0] == 1:
                await message.author.add_roles(discord.utils.get(message.guild.roles, name="Jail"))
            await message.channel.send(f'<@{message.author.id}> Bad Boi')
            await message.delete()
    if message.channel.name == 'mugs':
        rows = getRows(message.author.id)
        if len(rows) == 0:
            initUser(message.author.id)
        if "mugs" in message.content and len(message.content) == 4:
            row = getMugs(message.author.id)
            await message.channel.send(f'<@{message.author.id}> has {row[0]} mugs')
        else:
            rows = getRows(message.author.id)
            if len(rows) == 0:
                initUserJail(message.author.id)
            else:
                jailUser(message.author.id)
            jailed = getJailed(message.author.id)
            if jailed[0] == 1:
                await message.author.add_roles(discord.utils.get(message.guild.roles, name="Jail"))
            await message.channel.send(f'<@{message.author.id}> Bad Boi')
            await message.delete()
    if message.channel.name == 'jail':
        if "sorry" in message.content and len(message.content) == 5:
            updateSorryCount(message.author.id)
            sorry_count = getSorryCount(message.author.id)
            if sorry_count[0] >= 5:
                jailed = getJailed(message.author.id)
                resetSorryCount(message.author.id)
                setUserFree(message.author.id)
                await message.author.remove_roles(discord.utils.get(message.guild.roles, name="Jail"))
        else:
            await message.channel.send(f'<@{message.author.id}> Your efforts to rebel are futile.')
            await message.delete()

client.run(bot_token)