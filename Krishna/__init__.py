from pyrogram import Client

API_ID = int (28422427)
API_HASH = "9d83e9bc46cab0c6793faebbd324d4e3"
BOT_TOKEN = "6177593163:AAErW32P3kDJjLlnariSMuUragNWYC3bc4c"

#boot
app = Client (name="Okk", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True, plugins=dict(root="Krishna/plugins"))
