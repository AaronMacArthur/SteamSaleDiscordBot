from bs4 import BeautifulSoup
import requests
import re
import discord
from discord.ext import commands

TOKEN = 'TOKEN'
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents = intents)

URL = "https://gg.deals/deals/?minMetascore=80&store=4"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='page')
name_basic = str(results.find_all('a', class_='game-info-title title'))
price_basic = str(results.find_all('span', class_='price-inner game-price-new'))
discount_basic = str(results.find_all('span', class_='discount label'))
images_basic = results.find_all('picture', class_='game-picture')

names = str(re.sub('<.*?>', '', name_basic))
price = str(re.sub('<.*?>', '', price_basic))
discount = str(re.sub('<.*?>', '', discount_basic))
picture = str(images_basic)


ism = picture.split('"')
ns = names.split(',')
ps = price.split()
ds = discount.split()

nns = [re.sub(r'[^\w\s]', '', item) for item in ns]

pdn0 = (nns[0],"is only", ps[0], 'and is currently', ds[0], 'off')
pdn1 = (nns[1],"is only", ps[1], 'and is currently', ds[1], 'off')
pdn2 = (nns[2],"is only", ps[2], 'and is currently', ds[2], 'off')
pdn3 = (nns[3],"is only", ps[3], 'and is currently', ds[3], 'off')
pdn4 = (nns[4],"is only", ps[4], 'and is currently', ds[4], 'off')
pdn5 = (nns[5],"is only", ps[5], 'and is currently', ds[5], 'off')
pdn6 = (nns[6],"is only", ps[6], 'and is currently', ds[6], 'off')
pdn7 = (nns[7],"is only", ps[7], 'and is currently', ds[7], 'off')
pdn8 = (nns[8],"is only", ps[8], 'and is currently', ds[8], 'off')
pdn9 = (nns[9],"is only", ps[9], 'and is currently', ds[9], 'off')

pdnn0 = ' '.join([str(elem) for elem in pdn0])
pdnn1 = ' '.join([str(elem) for elem in pdn1])
pdnn2 = ' '.join([str(elem) for elem in pdn2])
pdnn3 = ' '.join([str(elem) for elem in pdn3])
pdnn4 = ' '.join([str(elem) for elem in pdn4])
pdnn5 = ' '.join([str(elem) for elem in pdn5])
pdnn6 = ' '.join([str(elem) for elem in pdn6])
pdnn7 = ' '.join([str(elem) for elem in pdn7])
pdnn8 = ' '.join([str(elem) for elem in pdn8])
pdnn9 = ' '.join([str(elem) for elem in pdn9])

print(ism[275])

@client.event
async def on_ready():
    print('BOT READY :D')

@client.command()
async def promo(ctx):
    channel = client.get_channel(804620689768185879)
    await channel.send(pdnn0)
    embed=discord.Embed(url=ism[23])
    embed.set_thumbnail(url=ism[23])
    await ctx.send(embed=embed)
    await channel.send(pdnn1)
    embed=discord.Embed(url=ism[51])
    embed.set_thumbnail(url=ism[51])
    await ctx.send(embed=embed)
    await channel.send(pdnn2)
    embed=discord.Embed(url=ism[79])
    embed.set_thumbnail(url=ism[79])
    await ctx.send(embed=embed)
    await channel.send(pdnn3)
    embed=discord.Embed(url=ism[107])
    embed.set_thumbnail(url=ism[107])
    await ctx.send(embed=embed)
    await channel.send(pdnn4)
    embed=discord.Embed(url=ism[135])
    embed.set_thumbnail(url=ism[135])
    await ctx.send(embed=embed)
    await channel.send(pdnn5)
    embed=discord.Embed(url=ism[163])
    embed.set_thumbnail(url=ism[163])
    await ctx.send(embed=embed)
    await channel.send(pdnn6)
    embed=discord.Embed(url=ism[191])
    embed.set_thumbnail(url=ism[191])
    await ctx.send(embed=embed)
    await channel.send(pdnn7)
    embed=discord.Embed(url=ism[219])
    embed.set_thumbnail(url=ism[219])
    await ctx.send(embed=embed)
    await channel.send(pdnn8)
    embed=discord.Embed(url=ism[247])
    embed.set_thumbnail(url=ism[247])
    await ctx.send(embed=embed)
    await channel.send(pdnn9)
    embed=discord.Embed(url=ism[275])
    embed.set_thumbnail(url=ism[275])
    await ctx.send(embed=embed)





client.run(TOKEN)
