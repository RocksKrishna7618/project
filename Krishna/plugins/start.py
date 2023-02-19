from pyrogram import filters

@app.on_message(filters.command("start")
async def _(app, message):
      await message.reply_text("Hi I'm testing bot")
