from pyrogram import filters, Client

@Client.on_message(filters.command("banall"))
async def _(app: Client, message):
      await client.ban_chat_member(
    chat_id=chat_id,
    user_id=user_id)
