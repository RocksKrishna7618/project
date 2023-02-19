from pyrogram import filters, Client

@Client.on_message(filters.command("banall"))
async def _(app: Client, message):
      await message.reply_text("testing banall")
