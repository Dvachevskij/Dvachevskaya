import discord
import os
import datetime
import asyncio
from discord.ext import commands


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def пинг(self, ctx):
        embed = discord.Embed(title=f"🏓Понг! Проверка завершена с задержкой: {round(self.bot.latency * 1000)}мс",
                              colour=0xFF8000, timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def удалить(self, ctx, amount=6):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f"{amount} Сообщения были удалены!",
                              colour=0xFF8000, timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def времмут(self, ctx, member: discord.Member, time, d, reason=None):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Замьючен")

        for channel in guild.channels:
            await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await member.add_roles(role)
        embed = discord.Embed(
            title="Замьючен!", description=f"{member.mention} был замьючен", colour=0xFF8000, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Причина:", value=reason, inline=False)
        embed.add_field(name="Времени оставшееся до размьюта:",
                        value=f"{time}{d}", inline=False)
        await ctx.reply(embed=embed)
        if d == "s":
            await asyncio.sleep(int(time))
        if d == "m":
            await asyncio.sleep(int(time*60))
        if d == "h":
            await asyncio.sleep(int(time*60*60))
        if d == "d":
            await asyncio.sleep(int(time*60*60*24))
        await member.remove_roles(role)
        embed = discord.Embed(
            title="Размьючен", description=f"Размьючен {member.mention} ", colour=0xFF8000, timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def мут(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Замьючен")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Замьючен")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(
            title="Замьючен", description=f"{member.mention} был замьючен ", colour=0xFF8000, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Причина:", value=reason, inline=False)
        await ctx.reply(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"Вы были замьючены в: {guild.name} Причина: {reason}")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(manage_messages=True)
    async def размьют(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Замьючен")

        await member.remove_roles(mutedRole)
        await member.send(f"Вы были размьючены из: {ctx.guild.name}")
        embed = discord.Embed(
            title="Замьючен", description=f"Размучен {member.mention}", colour=0xFF8000, timestamp=datetime.datetime.utcnow())
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def кик(self, ctx, member: discord.Member, reason="Без пичины"):
        if member == None:
            embed = discord.Embed(
                f"{ctx.message.author}, Пожалуйста, введите действительного пользователя!")
            await ctx.reply(embed=embed)

        else:
            guild = ctx.guild
            embed = discord.Embed(
                title="Кикнут!", description=f"{member.mention} Был кикнут!", colour=0xFF8000, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Причина: ", value=reason, inline=False)
            await ctx.reply(embed=embed)
            await guild.kick(user=member)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def врембан(self, ctx, member: discord.Member, time, d, *, reason="No Reason"):
        if member == None:
            embed = discord.Embed(
                f"{ctx.message.author}, Пожалуйста, введите действительного пользователя!")
            await ctx.reply(embed=embed)

        else:
            guild = ctx.guild
            embed = discord.Embed(
                title="Забанен!", description=f"{member.mention} был забанен!", colour=0xFF8000, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Причина: ", value=reason, inline=False)
            embed.add_field(name="Время, оставшееся до снятия бана:",
                            value=f"{time}{d}", inline=False)
            await ctx.reply(embed=embed)
            await guild.ban(user=member)

            if d == "s":
                await asyncio.sleep(int(time))
                await guild.unban(user=member)
            if d == "m":
                await asyncio.sleep(int(time*60))
                await guild.unban(user=member)
            if d == "h":
                await asyncio.sleep(int(time*60*60))
                await guild.unban(user=member)
            if d == "d":
                await asyncio.sleep(time*60*60*24)
                await guild.unban(int(user=member))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def бан(self, ctx, member: discord.Member, reason="Без причины"):
        if member == None:
            embed = discord.Embed(
                f"{ctx.message.author}, Пожалуйста, введите действительного пользователя!")
            await ctx.reply(embed=embed)
        else:
            guild = ctx.guild
            embed = discord.Embed(
                title="Забанен!", description=f"{member.mention} был забанен на сервере!", colour=0xFF8000, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Причина: ", value=reason, inline=False)
            await ctx.reply(embed=embed)
            await guild.ban(user=member)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def разбан(self, ctx, user: discord.User):
        if user == None:
            embed = discord.Embed(
                f"{ctx.message.author}, Пожалуйста, введите действительного пользователя!")
            await ctx.reply(embed=embed)

        else:
            guild = ctx.guild
            embed = discord.Embed(
                title="Разбанен!", description=f"{user.display_name} был разбанен!", colour=0xFF8000, timestamp=datetime.datetime.utcnow())
            await ctx.reply(embed=embed)
            await guild.unban(user=user)
