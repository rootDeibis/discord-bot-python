import discord


class DiscordBotBuilder(discord.Client):
    CommandManager = None

    async def on_ready(self):
        print(f"{self.user.name} ready!")
        
    async def on_message(self, message):
        args = message.content.split(" ")

        if message.author.id == self.user.id:
            return

        if message.content.startswith("!") == False: 
            return

        if self.CommandManager == None:
            return
        
        command = self.CommandManager.find_command(args[0].replace("!", ""))

        if( command != None):
            await command.handle(self, message, args)
