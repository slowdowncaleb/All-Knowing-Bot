import praw
import discord 
from discord.ext import commands
from random import randint,choice
client=commands.Bot(command_prefix= ",")

reddit = praw.Reddit(
    client_id="a3BHpd6NQhYLRQ",
    client_secret="eN12PGEGghZkhoYefAEzfGa3kVAnqQ",
    user_agent="redditpraw.py",
    username="Watermel0nb0t",
    password="WATERMELON",
    check_for_async=False,
)
reddit.read_only = True

#dank meme
@client.command()
async def dankmeme(ctx):
    memesubreddit = reddit.subreddit("dankmemes")
    message = choice([meme for meme in memesubreddit.hot(limit=50)])
    if "https://i.redd.it" in message.url:
        memeembed = discord.Embed(title=message.title,description=f"[link](https://www.reddit.com/r/{message.subreddit}/{message.id}/{message.title.replace(' ','_')}/)")
        memeembed.set_image(url=message.url)
        memeembed.set_footer(text=f"👍 {message.score} \nposted by u/{message.author.name}")
        await ctx.send(embed=memeembed)
    else:
        await ctx.send("ouch this post wasn't a meme try again lmfao")

#dumb meme
@client.command()
async def meme(ctx):
    memesubreddit = reddit.subreddit("memes")
    message = choice([meme for meme in memesubreddit.hot(limit=50)])
    if "https://i.redd.it" in message.url:
        memeembed = discord.Embed(title=message.title,description=f"[link](https://www.reddit.com/r/{message.subreddit}/{message.id}/{message.title.replace(' ','_')}/)")
        memeembed.set_image(url=message.url)
        memeembed.set_footer(text=f"👍 {message.score} \nposted by u/{message.author.name}")
        await ctx.send(embed=memeembed)
    else:
        await ctx.send("ouch this post wasn't a meme try again lmfao")

#wholesomememes
#AdviceAnimals

client.run("NzY5OTY4NzU3NDQyNjA5MjEz.X5WvSQ.xnPk0Oqd_07qPHchSTYpsdRL3ck")