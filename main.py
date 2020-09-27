import discord

from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

bot = commands.Bot(command_prefix='!')


@bot.command(name='say', pass_context=True)
@has_permissions(administrator=True)
async def say(ctx, arg):
    await ctx.send(arg)


@bot.command(name='test', pass_context=True)
async def test_command(ctx):
    embed = discord.Embed(title='Test', description='Test')
    await ctx.send(embed=embed)


@bot.command(name='ban', pass_context=True)
@has_permissions(administrator=True)
async def ban_command(ctx, member: discord.Member = None, reason=None):
    if member == None or member == ctx.message.author:
        return
    if reason == None:
        reason = "Gebannt"
    await ctx.guild.ban(member, reason=reason)
    embed = discord.Embed(title='<a:achtung:759389989657772042> User verbannt!',
                          description='**{0}** wurde vom **junghema.de** Server verbannt.'.format(str(member)))
    await ctx.channel.send(embed=embed)


@bot.command(name='kick', pass_context=True)
@has_permissions(administrator=True)
async def kick_command(ctx, member: discord.Member = None, reason=None):
    if member == None or member == ctx.message.author:
        return
    if reason == None:
        reason = "Gekickt"
    await ctx.guild.kick(member, reason=reason)
    embed = discord.Embed(title='<a:achtung:759389989657772042> User gekickt!',
                          description='**{0}** wurde vom Server gekickt.'.format(str(member)))
    await ctx.channel.send(embed=embed)


@bot.event
async def on_member_join(member):
    embed = discord.Embed(description=f'<a:pfeil:759389901061488650> {member.mention} ist hier! Begrüßt {member.mention}')
    await bot.get_channel(759368202093330482).send(embed=embed)


@bot.event
async def on_message(message):
    if message.channel.id == '759364128984530945':
        check = bot.get_emoji(759392047689498665)
        yes_or_no = bot.get_emoji(739204828328361984)
        cross = bot.get_emoji(759392063099109406)
        await message.add_reaction(check)
        await message.add_reaction(yes_or_no)
        await message.add_reaction(cross)

bot.run('token')
