import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Yud")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/96ce42b289252717b57f5.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "YudAssistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "VcgSupportGroup")
PROJECT_NAME = getenv("PROJECT_NAME", "Geez Mudic Project")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/yud023/Geez-MusicProject")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
