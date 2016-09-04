import discord
from random import choice as randchoice
from discord.ext import commands

class Responses:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
    	self.bot = bot

    	self.lewd = ["https://i.imgur.com/SXghDXf.png", "https://i.imgur.com/x55ugV5.png", "https://i.imgur.com/z6Me1y3.png", "https://i.imgur.com/oK7igKC.jpg", "https://i.imgur.com/DC4AVNJ.png", "https://i.imgur.com/oC66kCP.jpg", "https://i.imgur.com/r140Nbr.jpg"]

    @commands.command()
    async def marco(self):
    	"""Marco - Polo"""
    	await self.bot.say("Polo!")

    @commands.command()
    async def on_message(self, message):
    #.lower() - remember to have the "string" all in lower caps
    	if "kms" in message.content.lower():
    		await self.bot.send_message(message.channel, "kys")

    	if "nico-nico-nii!" in message.content.lower():
    		await self.bot.send_message(message.channel, "https://i.imgur.com/lqSm7gk.gif")
    	
    	if "desu" in message.content.lower():
    		await self.bot.send_message(message.channel, "WEEB!")

    	if "lewd" in message.content.lower():
    		await self.bot.send_message(message.channel, randchoice(self.lewd))	

    	if "salt" in message.content.lower() and message.server.me.id != message.author.id:#Prevents spam by checking if the message sender is 
    		await self.bot.send_message(message.channel, "PJSalt") #bot.send_message if NOT command

def setup(bot):
    bot.add_cog(Responses(bot))