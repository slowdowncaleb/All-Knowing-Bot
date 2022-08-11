import discord 
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from random import *
import asyncio
import time
client=commands.Bot(command_prefix= ",")

def get_random_color():
    number_of_colors = 1

    color = ["#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    almost_final_color = color[0][1:]
    final_color='0x' + almost_final_color
    return final_color

#on join
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        await channel.send(f"Hello people of {guild}! I'm the all-knowing bot! invite me other server as well!\nhttps://discord.com/oauth2/authorize?client_id=769968757442609213&scope=bot&permissions=8")
        role=await guild.create_role(name="Muted",permissions=discord.Permissions(permissions=68224064))
        for channel in guild.channels:
            perms = channel.overwrites_for(role)
            perms.send_messages = False
            perms.add_reactions = False
            await channel.set_permissions(role, overwrite=perms, reason="Muted!")

#start
@client.event
async def on_ready():
    print("bot is running")
    await client.change_presence(activity=discord.Game("---"))
    #channel=client.get_channel(788648908753862658)
    #await channel.send("#general The BOT is in the house! Please support my developer Caleb by sending him money")
    #await channel.send("https://tenor.com/view/baby-yoda-baby-yoda-wave-baby-yoda-waving-hi-hello-gif-15975082")

#8ball
@client.command(aliases=["8ball","8b"])
async def _8ball(ctx,*,q:str=None):
    if q==None:
        await ctx.message.channel.send("bruh ask a question or this is useless :unamused:")
    else:
        responses= ["It is certain.","It is decidedly so.","Without a doubt.","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful.","What do you think I am, a omniscient fortune teller?"]
        msg=discord.Embed(title=str(client.get_user(ctx.message.author.id))+" asks "+q,description="the magic 8ballz say: "+choice(responses),color=0x000000)
        msg.set_footer(text="ask the magic 8ball more-it is always right", icon_url=ctx.author.avatar_url)
        await ctx.message.channel.send(embed=msg)

#clear
@client.command("clear")
async def clear(ctx,text):
    amount=int(text)
    await ctx.channel.purge(limit=amount)

#emoji
@client.command("emoji")
async def emoji(ctx, *,text):
    splitMsg=text.split()
    e=splitMsg[0]
    splitMsg.pop(0)
    if len(splitMsg) == 1:
        splitMsg = list(splitMsg[0])
    finalMsg = [e + " "]
    for word in splitMsg:
        finalMsg.append(word)
        finalMsg.append(" " + e + " ")
    await ctx.message.channel.send(''.join(finalMsg))

#emojify
@client.command("emojify")
async def emojify(ctx, *,text):
    output=""
    for letter in text:
        if letter not in [",",";",":"," ",".","(",")","!"]:
            output+=" :regional_indicator_"+letter.lower()+": "
    await ctx.message.channel.send(output)

#mock
@client.command('mock')
async def mock(ctx,*,text):
    await ctx.message.channel.send("ok then")
    text=text.lower()
    output=""
    x=0
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for letter in text:
        x+=1
        if x%2==0 and letter in lower:
            output+=letter
        if x%2==1 and letter in lower:
            output+=upper[lower.index(letter)]
        elif letter not in lower:
            output+=letter
            x-=1
    await ctx.message.channel.send(output)

#snipe
snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@client.event
async def on_message_delete(message):
    
    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

#plz snipe
@client.command("snipe")
async def snipe(ctx):
    global snipe_message_content
    global snipe_message_author
    
    if snipe_message_content==None:
        await ctx.message.channel.send("lol wtf there is nothing to snipe no more try to be faster next time :smirk:")
    else:
        msg=discord.Embed(title=str(client.get_user(snipe_message_author)) + " said", description=snipe_message_content, color=0x0047ab)
        msg.set_footer(text=f"Asked by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        await ctx.message.channel.send(embed=msg)

#guess game
@client.command("guess")
async def guess(ctx):
    num=randint(1,20)
    await ctx.message.channel.send("pick a number from one to twenty")
    for i in range(1,4):
        ans = await client.wait_for("message")
        while ans.author!=ctx.message.author:
            ans = await client.wait_for("message")
        if int(ans.content) == num:
            await ctx.send("man you are too good for me. but you only won this battle-you wont win the war")
            break
        elif int(ans.content) > num:
            await ctx.message.channel.send(f"you are too big :smirk: . you have {3-i} tries left")
        elif int(ans.content) < num:
            await ctx.message.channel.send(f"you are too small :smirk: . you have {3-i} tries left")
    else:
        await ctx.message.channel.send(f"nice you lost. are you proud? the number was {num}")

#dice 
@client.command(aliases=["dice","roll"])
async def _dice(ctx,a:int=1,b:int=6):
    text=""
    num=0
    try:
        for x in range(a):
            text+=f"{str(randint(1,b))},"
            num+=randint(1,b)
        msg=discord.Embed(title="dice roll",description=f"you rolled {text[:-1]}\nthe sum of {a} rolls of a {b} sided die is {num}",color=int(get_random_color(),16))
        msg.set_footer(text=f"rolling for {ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=msg)
    except OverflowError:
        await ctx.send("too many repetitions - try less dice or a smaller die next time")
        return

#poll
@client.command("poll")
async def dm(ctx,*,text):
    number_emojis= [":zero:",":one:",":two:",":three:",":four:",":five:",":six:",":seven:",":eight:",":nine:"]
    content=text.split(",")
    msg=discord.Embed(title=content[0],description="|||||",color=0xFFD700)
    msg.set_footer(text=f"Asked by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    content.pop(0)
    x=0
    for member in content:
        x+=1
        try:
            msg.add_field(name=number_emojis[x]+" "+str(member), value="__", inline=False)
        except IndexError:
            await ctx.message.channel.send("too many options")
            return
    rng=await ctx.message.channel.send(embed=msg)
    emoji_list=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"]
    for y in range(x):
        await rng.add_reaction(emoji_list[y])
    pollclose=False


#tic tac toe
def win(game_board):
    winner = None
    if game_board[6] == game_board[7] == game_board[8]:
       winner = game_board[6]
    if game_board[3] == game_board[4] == game_board[5]:
       winner = game_board[3]
    if game_board[0] == game_board[1] == game_board[2]:
       winner = game_board[0]
    if game_board[0] == game_board[3] == game_board[6]:
       winner = game_board[0]
    if game_board[1] == game_board[4] == game_board[7]:
       winner = game_board[1]
    if game_board[2] == game_board[5] == game_board[8]:
       winner = game_board[2]
    if game_board[6] == game_board[7] == game_board[8]:
       winner = game_board[4]
    if game_board[0] == game_board[4] == game_board[8]:
       winner = game_board[0]   
    return winner

#plz tictactoe
@client.command("tictactoe")
async def tictactoe(ctx):
    Embed=discord.Embed(title="choose a number from one to nine to choose your space by typing into chat press end to end the game YOU ARE X",description="1|2|3\n4|5|6\n7|8|9")
    Embed.set_footer(text=f"{ctx.author.name}'s game", icon_url=ctx.author.avatar_url)
    msg = await ctx.message.channel.send(embed=Embed)
    gameboard=[str(y) for y in range(1,10)]
    x=0
    while x<9:
        if x%2==0:
            while True:
                ans = await client.wait_for("message")
                while ans.author!=ctx.message.author:
                    ans = await client.wait_for("message")
                if ans.content=="end":
                    Embed=Embed=discord.Embed(title="choose a number from one to nine to choose your space by typing into chat YOU ARE X",description="GAME ENDED")
                    Embed.set_footer(text=f"{ctx.author.name}'s game", icon_url=ctx.author.avatar_url)
                    await msg.edit(embed=Embed)
                    return
                try:
                    if gameboard[int(ans.content)-1] == "X" or gameboard[int(ans.content)-1] == "O":
                        await ctx.send("can't put there... space alr taken")
                    else:
                        gameboard[int(ans.content)-1]="X" 
                        break
                except ValueError:
                    await ctx.send("dude has to be a integer or end")
            
        else:
            ans = randint(0,8)
            while gameboard[ans]=="O" or gameboard[ans]=="X":
                ans = randint(0,8)
            gameboard[ans]="O"
        x+=1
        text=""
        winner=win(gameboard)
        for Z in range(9):
            text+=f"{gameboard[Z]}|"
            if Z%3==2:
                text=text[:-1]+"\n"
        if winner!=None:
                text+=f"\ngame ended the winner of this game is player {winner}"
                Embed=Embed=discord.Embed(title="choose a number from one to nine to choose your space by typing into chat YOU ARE X",description=text)
                Embed.set_footer(text=f"{ctx.author.name}'s game", icon_url=ctx.author.avatar_url)
                await msg.edit(embed=Embed)
                return
        Embed=Embed=discord.Embed(title="choose a number from one to nine to choose your space by typing into chat type end to end YOU ARE X",description=text)
        Embed.set_footer(text=f"{ctx.author.name}'s game", icon_url=ctx.author.avatar_url)
        await msg.edit(embed=Embed)
    else:
        text+="\nu tied with a bot arent u sad"
        Embed=Embed=discord.Embed(title="choose a number from one to nine to choose your space by typing into chat type end to end YOU ARE X",description=text)
        Embed.set_footer(text=f"{ctx.author.name}'s game", icon_url=ctx.author.avatar_url)
        await msg.edit(embed=Embed)

#hangman
def pickword():
    inFile = open("words.txt", 'r')
    line = inFile.readline()
    wordlist = line.split()
    word = choice(wordlist)
    return word

#plz hangman
@client.command("hangman")
async def hangman(ctx):
    word=pickword()
    guess="-"*len(word)
    alphabet=[chr(x) for x in range(97,123)]
    emb=discord.Embed(title="hangman",description=guess)
    emb.set_footer(text=f"{ctx.author.name}'s game (type 'end' to end and 'update' to resend)", icon_url=ctx.author.avatar_url)
    msg= await ctx.send(embed=emb)
    turn=0
    while turn!=5:
        ans=await client.wait_for("message")
        while len(ans.content)>1 or (ans.content not in alphabet) or ans.author!=ctx.message.author:
            if ans.author!=ctx.message.author:
                pass
            elif ans.content==word:
                emb=discord.Embed(title="hangman",description=f"{word}\n\nYOU WON with {turn} incorrect guesses")
                emb.set_footer(text=f"{ctx.author.name}'s game (type 'end' to end and 'update' to resend)", icon_url=ctx.author.avatar_url)
                await msg.edit(embed=emb)
                return
            elif len(ans.content)>1:                
                if ans.content=="update":
                    await ctx.send(embed=emb)
                elif ans.content=="end":
                    return
                else:
                    await ctx.send("only one letter no cheating try again")
            elif ans.content not in alphabet:
                await ctx.send("you already chose this")
            ans=await client.wait_for("message")
        inword=False
        for x in range(len(word)):
            if ans.content==word[x]:
                guesslist=list(guess)
                guesslist[x]=word[x]
                guess="".join(guesslist)
                inword=True
        if guess==word:
            guess+=f"\n\nYOU WON with {turn} incorrect guesses"
        alphabet[alphabet.index(ans.content)]="-"
        emb=discord.Embed(title="hangman",description=guess)
        emb.set_footer(text=f"{ctx.author.name}'s game (type 'end' to end and 'update' to resend)", icon_url=ctx.author.avatar_url)
        await msg.edit(embed=emb)
        if inword==False:
            turn+=1
            await ctx.send(f"lol try again you have {5-turn} tries left")    
    if turn>=5:
       emb=discord.Embed(title="hangman",description=f"{guess}\n\nyou lost haha the word was {word}")
       emb.set_footer(text=f"{ctx.author.name}'s game (type 'end' to end and 'update' to resend)", icon_url=ctx.author.avatar_url)
       await msg.edit(embed=emb)

#plz mute
@client.command("mute")
async def mute(ctx,member:discord.Member=None,*,reason):
    Muted=discord.utils.get(ctx.guild.roles, name="Muted")
    if member.id==726489329752342671:
        await ctx.send("can mute the dev man :smirk:")
        return
    if member==ctx.message.author or member==None:
        await ctx.send("cant mute yourself")
        return
    if  Muted >= ctx.author.top_role:
        await ctx.send("can't mute a mod")
        return
    try:
        await member.add_roles(Muted)
        await ctx.send(f"successfully muted {member} for reason: {reason}")
    except:
        await ctx.send(f"could not mute {member}")

@client.command("unmute")
async def unmute(ctx,member:discord.Member=None):
    if member==ctx.message.author or member==None:
        await ctx.send("cant unmute yourself")
        return
    try:
        Muted=discord.utils.get(ctx.guild.roles, name="Muted")    
        await member.remove_roles(Muted)
        await ctx.send(f"{member} unmuted. enjoy your newfound freedom of speech.")
    except:
        await ctx.send(f"looks like we cant unmute {member}, maybe they are already unmuted")

#plz kick
@client.command("kick")
async def kick(ctx,member:discord.Member=None,*,why=None):
    try:
        if ctx.author.guild_permissions.administrator:
            if member.id==726489329752342671:
                await ctx.message.channel.send("you can't kick the developer")
                return
            if member==None:
                await ctx.message.channel.send("noone kicked")
            await member.kick(reason=why)
            await ctx.send(f"{ctx.message.author} has kicked {member} rip")
    except MissingPermissions:
        await ctx.send("you dont have the perms lol")



client.run("NzY5OTY4NzU3NDQyNjA5MjEz.X5WvSQ.xnPk0Oqd_07qPHchSTYpsdRL3ck")