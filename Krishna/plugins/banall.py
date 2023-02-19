from pyrogram import filters, Client

@Client.on_message(filters.command("banall") & filters.group)
async def ban_all(_,msg):
    chat_id=msg.chat.id    
    bot=await Client.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True    
    if bot_permission:
        async for member in Client.get_chat_members(chat_id):       
        try:
             await Client.ban_chat_member(chat_id, member.user.id)
             await msg.reply_text(f"ғᴜᴄᴋɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴍᴏᴍs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {member.user.mention}")                    
        except Exception:
         pass
     else:
             await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")  
