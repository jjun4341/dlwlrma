import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import Context
import os

# Made By discord 땅콩#0531


def is_command(bot: Bot, msg: discord.Message) -> bool:
    cmds = []  # the bot's all command 
    for i in bot.all_commands:
        cmds.append(str(bot.command_prefix) + i)
    if msg.content in cmds:
        return True
    else:
        return False


def is_owner(bot: Bot, user: int) -> bool:
    owner_id: list = bot.owner_ids
    if user in owner_id:
        return True
    else:
        return False


async def add_cmd(bot: Bot, name: str) -> discord.Message:
    ctx = Context
    await ctx.send('please enter codes')
    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author
    desc = await bot.wait_for("message", check=check)
    if os.path.isdir(f'{os.getcwd()}/cogs/'):
        with open(f'{os.getcwd()}/cogs/{name}.py', 'w', encoding="UTF-8") as f:
            f.write(desc.content)
        bot.load_extension(f'cogs.{name}')
    elif os.path.isdir(f'{os.getcwd()}/Cogs/'):
        with open(f'{os.getcwd()}/Cogs/{name}.py', 'w', encoding="UTF-8") as f:
            f.write(desc.content)
        bot.load_extension(f'Cogs.{name}')
    return await ctx.send('Load Completed.')


def reload_all_exts(bot: Bot) -> None:
    if os.path.isdir(f'{os.getcwd()}/cogs/'):
        exts = [file for file in os.listdir(f'{os.getcwd()}/cogs/') if file.endswith(".py")]
        for i in exts: bot.reload_extension(i)

    elif os.path.isdir(f'{os.getcwd()}/Cogs/'):
        exts = [file for file in os.listdir(f'{os.getcwd()}/Cogs/') if file.endswith(".py")]
        for i in exts: bot.reload_extension(i)
    return


def cmd(*, cmds: str) -> None:
    os.popen(cmds)
    return


def error_handler() -> discord.Embed:
    async def on_command_error(ctx: Context, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='오류 발생 An Error has Occurred',
                description='Missing Permissons 권한이 부족합니다.',
                color=discord.Colour.red()
            )
            return embed