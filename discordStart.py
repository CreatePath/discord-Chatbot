import discord
from discord.ext import commands
from Token.token import token
from functions.webCrolling import exp_url
from functions.orderList import orderList

# ./ 로 시작하면 명령어로 인식
bot = commands.Bot(command_prefix="./")

@bot.event
async def on_ready():
    print("로그인중입니다. ")
    print(f"봇={bot.user.name}로 연결중")
    print("연결이 완료되었습니다.")
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 명령어모음(ctx):
    msg = orderList()
    await ctx.send(msg)

# hi 또는 안녕 명령어 처리
@bot.command(aliases=["hi"])
async def 안녕(ctx):
    await ctx.send("오니짱! 어서와!")

# 따라하기 명령어 처리
@bot.command()
async def 따라하기(ctx,*,text):
    await ctx.send(text)

# 명령어 하나로 물리학과 홈페이지에서 원하는 물리 실험의 보고서 링크 가져오기.
@bot.command()
async def 물리실험(ctx,experimentName):
    msg = exp_url(experimentName)
    await ctx.send(msg)

@bot.command()
async def 백준뽑기(ctx):
    # 사용자 입력을 어떻게 받지...?
    pass

bot.run(token)