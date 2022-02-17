import discord
import random
from discord.ext import commands
from random import randint
import string
import ascii
from discord.utils import get
from discord_webhook import DiscordWebhook
import time
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio

bot = commands.Bot(command_prefix='+', description='Generates proof')
@bot.event
async def on_ready():
    print(("-")*40)
    print('Logged in as')
    print(bot.user.name)
    print(("-")*40)
bot.remove_command("help") 
from discord.ext import commands
@bot.event
async def on_ready():
    activity = discord.Game(name="Dm me to claim!", type=2)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("DM to claim!")
serverinv = 'https://discord.gg/ZKTkjD6F'
@bot.event
async def on_message(message):
    embedVar = discord.Embed(title=":gift: Congratulations on inviting!", description="", color=1127128)
    embedVar.set_footer(text="I will dm you with your reward when it is your turn!")
    embedVar.add_field(name="New member in queue!", value=f'I have succesfully added a new member to the <#943852095562461205>!', inline=True)
    embedr = discord.Embed(title="Thank you for the DM!", description="🎈 You have been added to the queue in <#931760775528337458>!\n🎪 If you wish to claim faster, just invite __3 more people__ to the server below!", value='https://discord.gg/ZKTkjD6F', color=1127128)
    embedr.set_footer(text="I will dm you with your reward when it is your turn!")
    embedr.add_field(name=f"\nDO NOT SPAM", value=f'❗__Spamming my dms will remove you fom the waiting list__!\n\n🎉 https://discord.gg/ZKTkjD6F', inline=True)
    if message.author == bot.user:
        return
    if not message.guild:
        try:
          time.sleep(.7)
          async with message.channel.typing():
            time.sleep(5)
            await message.channel.send (embed = embedr)
            chanel = bot.get_channel(943852095562461205)
            await chanel.send (embed = embedVar)
        except discord.errors.Forbidden:
            pass
    else:
        pass
    await bot.process_commands(message)
@bot.command()
async def announce(ctx, channel: discord.TextChannel, args):
		await channel.send(args)
@bot.command()
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()

    else:
        await ctx.send(f"No channel named {channel.name} was found!") 
bot.run('OTQwMTIyNTM2MzQ2Mjc1ODUw.YgCzVw.xQalZP0xvS0TnfMul-BuNlqjbAE')
