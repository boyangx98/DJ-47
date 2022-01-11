import discord
from discord.ext import commands
from music import Player

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

bot.add_cog(Player(bot))

bot.run('OTMwNDg5MjUyODA5MTU0NjIz.Yd2npQ.5rQI0XYszA55p3AjLnm6yEW7tTs')
