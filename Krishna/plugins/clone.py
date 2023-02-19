from pyrogram import filters, Client
from Krishna import app, API_ID, API_HASH

@app.on_message(filters.private & filters.command("clone"))
async def _(app, message):
     reply = await message.reply("Usage:\n\n/clone <token>")
     token = message.command[1]
     try:
         await reply.edit("Booting Your Client")
         client = Client (name="Okk", api_id=API_ID, api_hash=API_HASH, bot_token=token in_memory=True, plugins=dict(root="Krishna/plugins"))
         await client.start()
         await reply.edit("Your Client Booted Successfully")
     except Exception as e:
         await reply.edit("Error:\n`{e}`")
