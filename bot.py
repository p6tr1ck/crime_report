import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!', token='MTEwMzg2MDkyNTYxNTg0OTQ5Mg.GmcvG2.Tvj9N3FKnu6YbXjjd2IQOg07C730AwZPi_rcX4')


async def send_message():
    channel = bot.get_channel(1103870425315934323)
