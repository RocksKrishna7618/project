from pyrogram import Client

API_ID = int (28422427)
API_HASH = "9d83e9bc46cab0c6793faebbd324d4e3"
BOT_TOKEN = "6077291057:AAGNCwquAFJ1gh1K_Px3Cteth4jXhiFLBA8"

#boot
app = Client (name="Okk", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True, plugins=dict(root="Krishna/plugins"))
