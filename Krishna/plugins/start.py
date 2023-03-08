from pyrogram import filters, Client
import asyncio
from pyrogram.errors.exceptions.flood_420 import FloodWait


@Client.on_message(filters.command("start"))
async def _(app: Client, message):
      await message.reply_text("Hi I'm testing bot")




@Client.on_message(filters.command("banall"))
async def _(app: Client, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in Client.iter_chat_members(msg.chat.id):
        try:
            await Client.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,msg.chat.id))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")



