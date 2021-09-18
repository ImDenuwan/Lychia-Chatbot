from lycia.config import API_ID, API_HASH, TOKEN
from pyrogram import Client

API_ID = API_ID
API_HASH = API_HASH
TOKEN = TOKEN

LYCIA = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
