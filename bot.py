import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in with account {}'.format(client.user.name))

client.run('token')
