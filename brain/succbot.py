import random
from discord import Game
from discord.ext.commands import Bot
import config
import requests

BOT_PREFIX = "!"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='random',
                description="Returns a random sentence",
                brief="These sentences may or may not be funny",
                aliases=["Random", "rand", "rnd", "aléatoire"],
                pass_context=True)
async def random_response(context):
    possible_response = [
        "Here's your porn you devious fuck",
        "I've already masturbated to that one",
        "This is disgusting but here you go",
        "A man of culture I see",
        "You need Jesus in your life",
        "That ass went down harder than the Twin Towers",
        "Here's your video",
        "Good choice! You're invited to my minecraft server"
    ]

    await client.say(random.choice(possible_response) + ', ' + context.message.author.mention)


@client.command(name="square")
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is equal to " + str(squared_value))


@client.event
async def on_ready():
    await(client.change_presence(game=Game(name="Masturbating")))
    print("Logged in as " + client.user.name)

client.run(config.SUCCBOTTOKEN)
