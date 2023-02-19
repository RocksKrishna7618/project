from pyrogram import filters, Client

@Client.on_message(filters.command("start"))
async def _(app: Client, message):
      await message.reply_text("Hi I'm testing bot")
