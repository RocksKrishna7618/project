from pyrogram import filters, Client

@Client.on_message(filters.command("/banall") & filters.group)
async def ban_all(_, msg):
    chat_id = msg.chat.id
    bot = await Client.get_chat_member(chat_id, "me")
    bot_permission = bot.status.is_admin and bot.status.permissions.can_restrict_members
    if bot_permission:
        async for member in Client.iter_chat_members(chat_id):
            try:
                await Client.kick_chat_member(chat_id, member.user.id)
                await msg.reply_text(f"Banned {member.user.mention} from the group.")
            except Exception as e:
                await msg.reply_text(f"Error banning {member.user.mention}: {e}")
    else:
        await msg.reply_text("Either I don't have the right to restrict users or you are not in sudo users.")
