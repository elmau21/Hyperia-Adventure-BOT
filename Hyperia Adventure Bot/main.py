import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import youtube_dl
import os
from random import choice
from discord.utils import get

bot = commands.Bot(command_prefix="$")
players  = {}


@bot.event 
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('Escribiendo Nuevas Aventuras'))
    print("Welcome to Hyperia")

@bot.event
async def on_member_join(ctx, *, member):
    channel = member.server.get_channel("788944900455399434")
    fmt = 'Bienvenid@ al Discord {1.name} De Hyperia Adventure, {0.mention}'
    await ctx.send_message(channel, fmt.format(member, member.server))

@bot.event
async def on_member_remove(member):
    print(f'{member} Se fué de nuestro mundo...')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Porfavor usa todos los argumentos.')

@bot.command()
async def Hola(ctx):
    msg = f'Hola! bienvenid@ al Servidor de Trabajo de Hyperia Adventure, esperamos que disfrutes trabajando con nosotros.'
    await ctx.send(msg)

@bot.command()
async def Artists(ctx):
    msg = f'Nuestros artistas son Vermillion Arts y Seira_1301'
    await ctx.send(msg)

@bot.command()
async def Diego(ctx):
    msg = f' Estimado {ctx.author.mention} Diego Ortíz es un informático, ​conocido por ser el autor del lenguaje de programación Python. Nació y creció en Paraguay. En el ambiente de los desarrolladores del lenguaje Python también se le conoce por el título BDFL (Benevolent Dictator for Life), teniendo asignada la tarea de fijar las directrices sobre la evolución de Python, así como la de tomar decisiones finales sobre el lenguaje que todos los desarrolladores acatan. Diego Ortíz tiene fama de ser bastante basado, realizando pocos cambios al lenguaje entre versiones sucesivas, intentando mantener siempre la compatibilidad con versiones anteriores. El 12 de julio de 2018, con un mensaje enviado a la lista de python-committers, anunció su retiro de los procesos de decisión. Desde noviembre del 2020 es parte de la División de Desarrolladores de la empresa ROBLOX'
    await ctx.send(msg)

@bot.command()
async def InfoDiego(ctx):
    msg = f'Diego Ortíz de Mérida Yucatán Perdió T H E G A M E'
    await ctx.send(msg)

@bot.command()
async def Dolla(ctx):
    msg = f'¡Puedes contratar al equipo de desarrollo Yuudai Team Development para desarrollar tú propio BOT para Discord, desde los 20 a 50 Dolares! (Dependiendo de lo que quieres que haga tú BOT)'
    await ctx.send(msg)

  
@bot.command()
async def Details(ctx):
    msg = f'{ctx.author.mention} Este BOT fué programado por: M͓̽ ͓̽a͓̽ ͓̽u͓̽#2914, siguelo en twitter:https://twitter.com/its_hiren_'
    await ctx.send(msg)

@bot.command()
async def InfoMau(ctx):
    msg = 'Mau PL, Programador y Escritor de Hyperia Adventure'
    await ctx.send(msg)

@bot.command()
async def InfoRafa(ctx):
    msg = 'Rafael E, Estudiante y Escritor de Hyperia Adventure'
    await ctx.send(msg)

@bot.command()
async def InfoArath(ctx):
    msg = 'Arath A, Escritor de Hyperia y Estudiante de Ingeniería Química.'
    await ctx.send(msg)

@bot.command()
async def Code01(ctx):
    msg = f' Escritores de Hyperia: Arath Aster, M͓̽ ͓̽a͓̽ ͓̽u͓̽, Rafael Freyre'
    await ctx.send(msg)

@bot.command()
async def Haruo(ctx):
    msg =f'¡Haruo!,¡Eres un Imbécil!'
    await ctx.send(msg)

@bot.command()
async def SrPug(ctx):
    msg = f'Haruo siempre patea al SrPug :c'
    await ctx.send(msg)

@bot.command()
async def Ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def POV(ctx):
    msg = f'POV Eres Diego y Nielsen esta cerca de ti OnO'
    await ctx.send(msg)

@bot.command()
async def Social(ctx):
    msg = f'https://twitter.com/HyperiaAccount'
    await ctx.send(msg) 

@bot.command()
async def Info(ctx):
    embed = discord.Embed(title="Help", description="Help command", color= 0x6da860)
    embed.add_field(name="Ping", value= f"{ctx.prefix}ping", inline=False)
    embed.add_field(name="website", value="**[Click Here](https://twitter.com/HyperiaAccount)**", inline=False)
    embed.add_field(name="Support", value="https://discord.gg/nqr3UFRJ")
    embed.set_author(name=f"{ctx.author.display_name}", url="https://infoupgrades.com/", icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Invoke By: {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_image(url=bot.user.avatar_url)
    await ctx.send(embed=embed)



keep_alive()
bot.run("Nzg4NTg3NTc5Nzc0OTkyMzg0.X9lrag.qYQNsyQnGIGtLJWSqDJJB_RQ-5I")