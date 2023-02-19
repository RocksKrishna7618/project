from pyrogram import filters, Client
from Krishna import app

@app.on_message(filters.private & filters.command("clone")
async def _(app, message):
     reply = await message.reply("Usage:\n\n/clone <token>")
     token = message.command[1]
     try:
         await reply.edit("Booting Your Client")
