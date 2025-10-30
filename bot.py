import discord
from discord.ext import commands
from modelo import get_class
#1 inmportacion de Discord

#permisos
intents = discord.Intents.default()
intents.message_content = True

#crear objeto bot
bot = commands.Bot(command_prefix= '!', intents=intents)
#prender bot
@bot.event
async def on_ready():
    print(F'{bot.user.name} se ha conectado a Discord')

#Primer comando
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for img in ctx.message.attachments:
            nombre_img = img.filename
            await img.save(f'imagenes/{nombre_img}')
            await ctx.send(get_class(
            model_path = "./keras_model.h5",
            labels_path = "labels.txt",
            image_path = f"imagenes/{nombre_img}"
        ))

    else: 
        await ctx.send('No hay imagenes')

token = ""
bot.run(token)