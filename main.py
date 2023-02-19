from pyrogram import Client, filters, idle

API _ID = int ()
API_HASH = ""
BOT_TOKEN = ""

#boot
app = Client (name="Okk", api_id=API_ID, api_hash=API_HASH, bot_token=BOT _TOKEN, in_memory=Ture)

#cmd running
@app.on_message(filters.command("start")
async def _(app, message):
      await message.reply_text("Hi I'm testing bot")

app.start()
idle()