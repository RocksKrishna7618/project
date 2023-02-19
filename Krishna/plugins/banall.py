from pyrogram import filters, Client
from Krishna import app 


@app.on_message(filters.command("banall", prefixes=".") & filters.group)
def ban_all_members(client, message):
    # Get the list of members in the group
    members = client.get_chat_members(message.chat.id)

    # Ban all members
    for member in members:
        try:
            client.kick_chat_member(message.chat.id, member.user.id)
        except:
            client.send_message(message.chat.id, f"An error occurred while trying to kick member {member.user.id}.")

    # Send a message to indicate that all members have been kicked
    client.send_message(message.chat.id, "All members have been kicked from this group.")
