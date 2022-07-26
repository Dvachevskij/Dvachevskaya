import discord
from discord.ext import commands, tasks
import random
from discord.utils import get
import traceback
import sys

from music_cogs import music_cog
from mod_cogs import Mod


token = 'OTk4OTg2Njk5ODA1ODI3MTQy.Glr060.TxlfJ3KOrn3BE0rddxaFd0t0dCRPFejTME94_M'

bot = commands.Bot(command_prefix='!')
client = commands.Bot(command_prefix='!')
bot.remove_command("help")
bot.add_cog(music_cog(bot))
bot.add_cog(Mod(bot))


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def очистить(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def обнять(ctx, user: discord.User = None, *, Notes=None):
    gifs = ['https://i.gifer.com/AmeN.gif', 'https://acegif.com/wp-content/uploads/hugs-5.gif',
            'https://acegif.com/wp-content/uploads/hugs-11.gif', 'https://i.gifer.com/YW.gif', 'https://i.gifer.com/U9L1.gif', 'https://i.gifer.com/27tM.gif', 'https://i.gifer.com/BIbM.gif', 'https://i.gifer.com/3a9O.gif']
    embedd = discord.Embed(
        title=" ", description=f"{ctx.message.author.mention} обнял {user.mention}", colour=0xFF8000)
    embedd.set_image(url=random.choice(gifs))

    if Notes is None:
        await ctx.send(embed=embedd)
    else:
        embedZ = discord.Embed(
            title=" ", description=f"{ctx.message.author.mention} обнял {user.mention}, {Notes}", colour=0xFF8000)
    embedZ.set_image(url=f"{random.choice(gifs)}")
    await ctx.send(embed=embedZ)


@bot.command()
async def поцеловать(ctx, user: discord.User = None, *, Notes=None):
    gifs = ['https://acegif.com/wp-content/uploads/anime-kiss-17.gif', 'https://acegif.com/wp-content/uploads/anime-kissin-2.gif', 'https://acegif.com/wp-content/uploads/anime-kissin-16.gif', 'https://acegif.com/wp-content/uploads/anime-kissin-5.gif',
            'https://acegif.com/wp-content/uploads/anime-kissin-7.gif', 'https://acegif.com/wp-content/uploads/anime-kissin-8.gif', 'https://acegif.com/wp-content/uploads/anime-kissin-11.gif', 'https://acegif.com/wp-content/uploads/anime-kiss-37.gif']
    embedd = discord.Embed(
        title=" ", description=f"{ctx.message.author.mention} поцеловал {user.mention}", colour=0xFF8000)
    embedd.set_image(url=random.choice(gifs))

    if Notes is None:
        await ctx.send(embed=embedd)
    else:
        embedZ = discord.Embed(
            title=" ", description=f"{ctx.message.author.mention} поцеловал {user.mention}, {Notes}", colour=0xFF8000)
    embedZ.set_image(url=f"{random.choice(gifs)}")
    await ctx.send(embed=embedZ)


@bot.command()
async def ударить(ctx, user: discord.User = None, *, Notes=None):
    gifs = ['https://steamuserimages-a.akamaihd.net/ugc/796493539618599548/2EA38539B226E90B6C99B7EB7C2D57CB86EF59A2/?imw=512&amp;imh=284&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true', 'https://i.gifer.com/8UDl.gif',
            'https://pa1.narvii.com/7173/c6e1de87e67b7aa5bdb5d6f6684331abc5fa0329r1-720-360_hq.gif', 'https://giffiles.alphacoders.com/170/170176.gif', 'https://i.pinimg.com/originals/da/a2/39/daa239218364e811106223aff9ab22cd.gif']
    embedd = discord.Embed(
        title=" ", description=f"{ctx.message.author.mention} ударил {user.mention}", colour=0xFF8000)
    embedd.set_image(url=random.choice(gifs))

    if Notes is None:
        await ctx.send(embed=embedd)
    else:
        embedZ = discord.Embed(
            title=" ", description=f"{ctx.message.author.mention} ударил {user.mention}, {Notes}", colour=0xFF8000)
    embedZ.set_image(url=f"{random.choice(gifs)}")
    await ctx.send(embed=embedZ)


@bot.command()
async def выпить(ctx, user: discord.User = None):
    gifs = ['https://i.gifer.com/IcT8.gif', 'https://i.gifer.com/3332.gif',
            'https://i.gifer.com/9ys.gif', 'https://i.gifer.com/DEXS.gif', 'https://i.gifer.com/NG.gif','https://tenor.com/view/monkey-gif-19923815']
    embedd = discord.Embed(
        title=" ", description=f"{ctx.message.author.mention} закатил за воротник...", colour=0xFF8000)
    embedd.set_image(url=random.choice(gifs))
    await ctx.send(embed=embedd)


# Войс
initial_extensions = ['cogs.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        if after.channel.id == 999007151244726364:
            for guild in bot.guilds:
                maincategory = discord.utils.get(
                    guild.categories, id=997369715322265628)
                channel2 = await guild.create_voice_channel(name=f'Канал {member.display_name}', category=maincategory)
                await channel2.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                await member.move_to(channel2)

                def check(x, y, z):
                    return len(channel2.members) == 0
                await bot.wait_for('voice_state_update', check=check)
                await channel2.delete()


bot.run(token)
