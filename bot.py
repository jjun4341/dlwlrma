from main import *
from discord.ext.commands import Bot
import discord

bot = Bot(command_prefix='!', intents=discord.Intents.all(), owner_ids=[443734180816486441, 814373647506341968])


@bot.event
async def on_ready():
    print(f'{bot.user} is Ready.')


@bot.event
async def on_message(msg):
    if msg.author.id == bot.user.id:
        return
    if is_command(bot=bot, msg=msg):
        await bot.process_commands(msg)
        return
    else:
        return


@bot.command(name='isown')
async def _asdf(ctx):
    if is_owner(bot=bot, user=ctx.author.id):
        await ctx.send('ㅇ관리자임')
    else:
        await ctx.send('ㄴㄴ')


@bot.command(name='ad')
async def _add(ctx, name):
    await add_cmd(bot=bot, name=name)

bot.run('Nzk1ODYxMjU0NTUxNzY1MDE1.X_PhjQ.ysj8yyaTQVk3a2BG28JzlGfegDE')