import discord 
from discord.ext import commands
from random import *
from time import time
from PIL import Image,ImageFont,ImageDraw
import requests
import json

client=commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("running")

def words_to_pic(message,out_file):
    img=Image.open('empty file.png')
    draw=Image.Draw(img)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf',20)
    draw.text((0,0), message, (255,255,255), font=font)
    img.save(out_file)

@client.command("tr")
async def tr(ctx):
    r=requests.get("https://zenquotes.io/api/random").json()
    quote=r[0]['q']
    quote_author=r[0]['a']
    respondents=0
    race_embed= discord.Embed(title=f"-{ctx.author}'s Type Race-",description=f"{quote}")
    race_embed.set_footer(text=f"quote by {quote_author} ")
    await ctx.send(embed=race_embed)
    start=time()
    athletes=[]
    while respondents<=3 and time()-start<=120: #2 minute limit
        response=await client.wait_for("message")
        if response.content==quote and response.author not in [ath['name'] for ath in athletes]:
            respondents+=1
            if respondents==1:
                await response.add_reaction("🥇")
            elif respondents==2:
                await response.add_reaction("🥈")
            elif respondents==3:
                await response.add_reaction("🥉")
            athletes.append({'name':response.author,'time':(time()-start)})
    finish_embed = discord.Embed(title=f"{ctx.author}'s Type Race Results",description=f"{quote} - {quote_author}\n\n{athletes[0]['name']} wins")
    tempnum=1
    for athlete in athletes:
        finish_embed.add_field(name=f"{tempnum}. {athlete['name']}",value=f"{round(athlete['time'],2)} seconds\n{round(len(quote)/athlete['time']*60,2)} wpm")
        tempnum+=1
    await ctx.send(embed=finish_embed)

client.run("NzY5OTY4NzU3NDQyNjA5MjEz.X5WvSQ.xnPk0Oqd_07qPHchSTYpsdRL3ck")
    

