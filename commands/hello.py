import discord

class command():
    name = "hola"

    async def handle(self, client: discord.Client, message: discord.Message, args):
        await message.reply("Hola")