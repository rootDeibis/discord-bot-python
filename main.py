from discord import Intents, Client
from os import path, getenv
from command_manager import CommandManager as CMDManager
from bot_class import DiscordBotBuilder
from dotenv import load_dotenv


load_dotenv()

CommandManager = CMDManager()
CommandManager.load(path.join(path.dirname(__file__), "commands"))


intents = Intents.default()

intents.message_content = True
intents.guilds=True

BotClient = DiscordBotBuilder(intents=intents)
BotClient.CommandManager = CommandManager

BotClient.run("")

