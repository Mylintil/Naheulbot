from discord.ext import commands

bot = commands.Bot("/")

TOKEN = 'NzA2NDUxMTQzMjA2NjMzNDcy.Xq6cdw.1GuIMRd81QtDzCcs1WOq-rfX7LE'
@bot.command(pass_context=True)
async def hello(ctx):
    message_author = ctx.message.author
    message_channel = ctx.message.channel

    print("{} said hello".format(message_author))
    await ctx.send("Ah mais putain ta gueule!")

@bot.event
async def on_ready():
    print("The bot is READY!")
    print("Logged in as: {}".format(bot.user.name))

bot.run(TOKEN)
