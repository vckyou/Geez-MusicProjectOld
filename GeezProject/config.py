import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Vckyouuu")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/ad54dc991d9e41dbbe37d.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GeezAssistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "VcgSupportGroup")
PROJECT_NAME = getenv("PROJECT_NAME", "Geez Mudic Project")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Vckyou/Geez-MusicProject")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
