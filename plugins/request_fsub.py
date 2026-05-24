# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
import asyncio
import os
import random
import sys
import time
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode, ChatAction, ChatMemberStatus, ChatType
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, ChatMemberUpdated, ChatPermissions
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, InviteHashEmpty, ChatAdminRequired, PeerIdInvalid, UserIsBlocked, InputUserDeactivated, UserNotParticipant
from helper.database import rexbots
from config import *
from helper.database import *
from plugins.helper_func import *

# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
# Request force sub mode command
@Client.on_message(filters.command('fsub_mode') & filters.private & admin)
async def change_force_sub_mode(client: Client, message: Message):
    temp = await message.reply("<b><i>ᴡᴀɪᴛ ᴀ sᴇᴄ..</i></b>", quote=True)
    channels = await rexbots.show_channels()

    if not channels:
        return await temp.edit("<b>❌ ɴo ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴɴᴇʟs ғᴏᴜɴᴅ.</b>")

    buttons = []
    for ch_id in channels:
        try:
            chat = await client.get_chat(ch_id)
            mode = await rexbots.get_channel_mode(ch_id)
            status = "🟢" if mode == "on" else "🔴"
            title = f"{status} {chat.title}"
            buttons.append([InlineKeyboardButton(title, callback_data=f"rfs_ch_{ch_id}")])
        except:
            buttons.append([InlineKeyboardButton(f"⚠️ {ch_id} (Unavailable)", callback_data=f"rfs_ch_{ch_id}")])

    buttons.append([InlineKeyboardButton("ᴄʟᴏsᴇ ✖️", callback_data="close")])

    await temp.edit(
        "<b>⚡ sᴇʟᴇᴄᴛ ᴀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴛᴏɢɢʟᴇ ғᴏʀᴄᴇ-sᴜʙ ᴍᴏᴅᴇ:</b>",
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
# This handler captures membership updates (like when a user leaves, banned)
@Client.on_chat_member_updated()
async def handle_Chatmembers(client, chat_member_updated: ChatMemberUpdated):
    chat_id = chat_member_updated.chat.id

    if await rexbots.reqChannel_exist(chat_id):
        old_member = chat_member_updated.old_chat_member

        if not old_member:
            return

        if old_member.status == ChatMemberStatus.MEMBER:
            user_id = old_member.user.id

            if await rexbots.req_user_exist(chat_id, user_id):
                await rexbots.del_req_user(chat_id, user_id)

# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
# This handler will capture any join request to the channel/group where the bot is an admin
@Client.on_chat_join_request()
async def handle_join_request(client, chat_join_request):
    chat_id = chat_join_request.chat.id
    user_id = chat_join_request.from_user.id

    # print(f"[JOIN REQUEST] User {user_id} sent join request to {chat_id}")

    # Print the result of rexbots.reqChannel_exist to check if the channel exists
    channel_exists = await rexbots.reqChannel_exist(chat_id)
    # print(f"Channel {chat_id} exists in the database: {channel_exists}")

    if channel_exists:
        if not await rexbots.req_user_exist(chat_id, user_id):
            await rexbots.req_user(chat_id, user_id)
            # print(f"Added user {user_id} to request list for {chat_id}")

@Client.on_message(filters.command('addchnl') & filters.private & admin)
async def add_force_sub(client: Client, message: Message):
    temp = await message.reply("<b><i>ᴡᴀɪᴛ ᴀ sᴇᴄ..</i></b>", quote=True)
    args = message.text.split(maxsplit=1)

    if len(args) != 2:
        return await temp.edit(
            "<b>Usage:</b> <code>/addchnl -100XXXXXXXXXX</code>\n<b>ᴀᴅᴅ ᴏɴʟʏ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴀᴛ ᴀ ᴛɪᴍᴇ.</b>",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴄʟᴏsᴇ ✖️", callback_data="close")]])
        )

    try:
        channel_id = int(args[1])
    except ValueError:
        return await temp.edit("<b>❌ ɪɴᴠᴀʟɪᴅ ᴄʜᴀɴɴᴇʟ ɪᴅ!</b>")

    all_channels = await rexbots.show_channels()
    channel_ids_only = [cid if isinstance(cid, int) else cid[0] for cid in all_channels]
    if channel_id in channel_ids_only:
        return await temp.edit(f"<b>ᴄʜᴀɴɴᴇʟ ᴀʟʀᴇᴀᴅʏ ᴇxɪsᴛs:</b> <code>{channel_id}</code>")

    try:
        chat = await client.get_chat(channel_id)

        if chat.type != ChatType.CHANNEL:
            return await temp.edit("<b>❌ ᴏɴʏ ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴀʀᴇ ᴀʟʟᴏᴡᴅ.</b>")

        member = await client.get_chat_member(chat.id, "me")
        print(f"Bot status: {member.status} in chat: {chat.title} ({chat.id})")  # Debug

        # FIXED ENUM COMPARISON
        if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return await temp.edit("<b>❌ ʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ.</b>")

        # Get invite link
        try:
            link = await client.export_chat_invite_link(chat.id)
        except Exception:
            link = f"https://t.me/{chat.username}" if chat.username else f"https://t.me/c/{str(chat.id)[4:]}"

        await rexbots.add_channel(channel_id)
        return await temp.edit(
            f"<b>✅ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴɴᴇʟ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!</b>\n\n"
            f"<b>Name:</b> <a href='{link}'>{chat.title}</a>\n"
            f"<b>ID:</b> <code>{channel_id}</code>",
            disable_web_page_preview=True
        )

    except Exception as e:
        return await temp.edit(
            f"<b>❌ ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴅᴅ ᴄʜᴀɴɴᴇʟ:</b>\n<code>{channel_id}</code>\n\n<i>{e}</i>"
        )
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
# Delete channel
@Client.on_message(filters.command('delchnl') & filters.private & admin)
async def del_force_sub(client: Client, message: Message):
    temp = await message.reply("<b><i>ᴡᴀɪᴛ ᴀ sᴇᴄ..</i></b>", quote=True)
    args = message.text.split(maxsplit=1)
    all_channels = await rexbots.show_channels()

    if len(args) != 2:
        return await temp.edit("<b>Usage:</b> <code>/delchnl <channel_id | all></code>")

    if args[1].lower() == "all":
        if not all_channels:
            return await temp.edit("<b>❌ ɴᴏ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴɴᴇʟs ғᴏᴜɴᴅ.</b>")
        for ch_id in all_channels:
            await rexbots.del_channel(ch_id)
        return await temp.edit("<b>✅ ᴀʟʟ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴɴᴇʟs ʜᴀs ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ.</b>")

    try:
        ch_id = int(args[1])
    except ValueError:
        return await temp.edit("<b>❌ ɪɴᴠᴀʟɪᴅ ᴄʜᴀɴɴᴇʟ ɪᴅ</b>")

    if ch_id in all_channels:
        await rexbots.rem_channel(ch_id)
        return await temp.edit(f"<b>✅ ᴄʜᴀɴɴᴇʟ ʀᴇᴍᴏᴠᴇᴅ:</b> <code>{ch_id}</code>")
    else:
        return await temp.edit(f"<b>❌ ᴄʜᴀɴɴᴇʟ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ғᴏʀᴄᴇ-sᴜʙ ʟɪsᴛ:</b> <code>{ch_id}</code>")
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
# View all channels
@Client.on_message(filters.command('listchnl') & filters.private & admin)
async def list_force_sub_channels(client: Client, message: Message):
    temp = await message.reply("<b><i>ᴡᴀɪᴛ ᴀ sᴇᴄ..</i></b>", quote=True)
    channels = await rexbots.show_channels()

    if not channels:
        return await temp.edit("<b>❌ ɴᴏ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴɴᴇʟs ғᴏᴜɴᴅ.</b>")

    result = "<b>⚡ ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴɴᴇʟs:</b>\n\n"
    for ch_id in channels:
        try:
            chat = await client.get_chat(ch_id)
            link = chat.invite_link or await client.export_chat_invite_link(chat.id)
            result += f"<b>•</b> <a href='{link}'>{chat.title}</a> [<code>{ch_id}</code>]\n"
        except Exception:
            result += f"<b>•</b> <code>{ch_id}</code> — <i>Unavailable</i>\n"

    await temp.edit(result, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Close ✖️", callback_data="close")]]))





# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
