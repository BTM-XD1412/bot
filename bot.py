import discord
from discord.ext import commands

# Khởi tạo bot với prefix là '!'
intents = discord.Intents.default()
intents.members = True  # Bật intents để quản lý thành viên

bot = commands.Bot(command_prefix='!', intents=intents)

# Sự kiện khi bot đã sẵn sàng
@bot.event
async def on_ready():
    print(f'Bot đã sẵn sàng với tên: {bot.user.name}')

# Lệnh ban một thành viên
@bot.command()
@commands.has_permissions(ban_members=True)  # Kiểm tra quyền
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Đã ban {member.mention}')

# Lệnh kick một thành viên
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Đã kick {member.mention}')

# Lệnh để hiển thị thông tin bot
@bot.command()
async def info(ctx):
    await ctx.send(f'Tên bot: {bot.user.name}\nID bot: {bot.user.id}')

# Chạy bot
TOKEN = 'MTA1NzIxNzkxNzA1MTIxNTk3NA.Gwn_Fp.RVPKXhzSMfh3wNsHBLeBll0nKP_zgrybOpJtVw'  # Thay YOUR_BOT_TOKEN bằng token thực của bạn
bot.run(TOKEN)
