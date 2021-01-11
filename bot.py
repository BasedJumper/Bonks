from discord.ext import commands 
import discord
import asyncio
import robin_stocks as r
import pyotp


# dont look at this 
totp = pyotp.TOTP("your key").now()
login = r.login('username','password', mfa_code=totp)

#prefix for the bot 
bot = commands.Bot(command_prefix='!')
ask_price=[]
bid_price=[]











#pulls crypto info form RH
def getcrypto(pdata):
	historical_quotes =r.get_crypto_quote(pdata)
	return historical_quotes


#  bot is ready
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
#when a message is sent keep a log of it, then await for a command
@bot.event
async def on_message(message):
	print("Message:", message.content)
	await bot.process_commands(message)

#list of command functions 
@bot.command()
async def clear(ctx):
	await ctx.message.channel.purge()


bot.run('discord bot token')