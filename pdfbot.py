from pdfgene import generate_pdf_binary
import os
import re
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
pdf_name = "artifact.pdf"

def legal_url(url: str):
  pattern = r'^https:\/\/gachi-matome\.com\/deckrecipe-detail-dm\/\?tcgrevo_deck_maker_deck_id=+'
  return bool(re.match(pattern, url))


#Bot定義
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())



@client.event
async def on_ready():
  print('ログインしました')

@client.command()
async def test(ctx):
  await ctx.send("test")

@client.command()
async def pdfmake(ctx, *args):
  url = None
  ngr_option = False
  nsp_option = False
  active_option = []
  for arg in args:
    if arg == "-ngr":
      ngr_option = True
      active_option.append("GRなし")
    elif arg == "-nsp":
      nsp_option = True
      active_option.append("超次元なし")
    elif arg.startswith("http"):
      url = arg
  
  if (not legal_url(url)):
    print("illegal")
    await ctx.send("urlが不正です")
    return
  
  message = "生成中です"
  if active_option:
    message += f" (オプション: {', '.join(active_option)})"
  await ctx.send(message)
  pdf_binary = generate_pdf_binary(url=url, ngr_option=ngr_option, nsp_option=nsp_option)
  try:
    await ctx.send(file=discord.File(fp=pdf_binary, filename=pdf_name))
    await ctx.send(f"{ctx.author.mention} 生成完了しました")
  except discord.HTTPException as e:
    if e.code == 40005:
      await ctx.send(f"{ctx.author.mention} エラー: ファイルサイズが大きすぎて送信できませんでした。枚数を減らすか、圧縮設定を見直してください。")
    else:
      await ctx.send(f"{ctx.author.mention} 送信中にエラーが発生しました: {e}")
  except Exception as e:
    print(f"Unexpected error: {e}")
    await ctx.send("予期せぬエラーが発生しました。")

client.run(TOKEN)
