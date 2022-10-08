from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","DarkxMusic")
BOT_USERNAME = getenv("BOT_USERNAME", "K61TBot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "o_lU_o")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "UUBU0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/390d078bddeb22f38c69b.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e68855e3be3191ca84624.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5519241772").split()))
