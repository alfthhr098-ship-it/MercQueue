
```python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

queue = []
tickets = {}

@bot.event
async def on_ready():
 print(f'{bot.user} telah siap!')

@bot.command(name='queue', help='Membuat queue')
async def queue_command(ctx):
 if queue:
 await ctx.send('Antrean:')
 for i, user in enumerate(queue):
 await ctx.send(f'{i+1}. {user.mention}')
 else:
 await ctx.send('Antrean kosong!')

@bot.command(name='queue start', help='Membuat queue')
async def queue_start(ctx):
 global queue
 if len(queue) < 5:
 await ctx.send('Queue telah dimulai!')
 else:
 await ctx.send('Queue sudah penuh!')

@bot.command(name='queue leave', help='Menghilangkan diri dari queue')
async def queue_leave(ctx):
 if ctx.author in queue:
 queue.remove(ctx.author)
 await ctx.send(f'{ctx.author.mention} telah meninggalkan queue!')
 else:
 await ctx.send(f'{ctx.author.mention} tidak berada di queue!')

@bot.command(name='pull', help='Mengeluarkan satu orang dari queue', hidden=True)
@commands.has_permissions(administrator=True)
async def pull(ctx):
 if queue:
 user = queue.pop(0)
 channel = await ctx.guild.create_text_channel(f'ticket-{user.id}', category=ctx.guild.default_channel_category)
 await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
 tickets[user.id] = channel
 await ctx.send(f'{user.mention} telah dipanggil!')
 await channel.send(f'{user.mention} telah dipanggil!')
 else:
 await ctx.send('Antrean kosong!')

@bot.command(name='queue stop', help='Menghentikan queue', hidden=True)
@commands.has_permissions(administrator=True)
async def queue_stop(ctx):
 global queue
 queue = []
 await ctx.send('Queue telah dihentikan!')

bot.run('MTUyMTUzNTczMzUxOTg4MDM0Mg.G4MFVq.D227q8LW2jTdYAcHqJ0xUBKi1BuZ-pYZtm8in8')
```
