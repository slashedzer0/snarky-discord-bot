import os
import discord
from discord.ext import commands
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_USER_ID = os.getenv("TARGET_USER_ID")
GITHUB_PAT_TOKEN = os.getenv("GITHUB_PAT_TOKEN")

endpoint = "https://models.inference.ai.azure.com"
model_name = "Meta-Llama-3.1-8B-Instruct"
token = GITHUB_PAT_TOKEN

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)
client = ChatCompletionsClient(endpoint, AzureKeyCredential(token))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.id == int(TARGET_USER_ID):
        if not message.content or not message.content.strip():
            print(f"[DEBUG] Skipping empty message from {TARGET_USER_ID}")
            return
            
        print(f"[DEBUG] Message from target user {TARGET_USER_ID}: {message.content}")
        user_message = UserMessage(content=message.content)
        system_message = SystemMessage(content="You are a snarky anger translator that represent the following user message. Mock them as much as you can. Assume the user you mock don't have the ability to see your message and don't even know you're exist. Your messages is intended for the other discord members, NOT for the user you mocks. You can use proper discord text formatting for the outputs. Keep the messages short and concise. Avoid addressing the user by technical terms like 'CurrentUser' or 'User', just address them as 'this guy' or equivalent.")
        response = client.complete(
            messages=[system_message, user_message],
            temperature=1.0,
            top_p=1.0,
            max_tokens=500,
            model=model_name
        )
        await message.channel.send(response.choices[0].message.content)

bot.run(DISCORD_TOKEN)