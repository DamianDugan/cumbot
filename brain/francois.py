import discord
import config


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('birthday'):
        msg = 'Merci {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!francois'):
        msg = 'Francois est une merde'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.FRANTOKEN)
