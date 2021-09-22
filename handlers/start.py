from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@Miss_florence_bot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="[ ](https://telegra.ph/file/ba834db90aa69f8b17b31.mp4)**𝗛𝗘𝗟𝗟𝗢 𝗧𝗛𝗘𝗥𝗘 ♥️ {}!**\n\n**𝐓𝐇𝐈𝐒 𝐈𝐒 𝐀 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐁𝐎𝐓 𝐎𝐅 𝐅𝐋𝐎𝐑𝐄𝐍𝐙𝐀✨.**\n\n**💗 𝐀𝐥𝐥𝐨𝐰'𝐬 𝐘𝐨𝐮 𝐓𝐨 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐎𝐧 𝐆𝐫𝐨𝐮𝐩𝐬 𝐓𝐡𝐫𝐨𝐮𝐠𝐡 𝐓𝐡𝐞 𝐍𝐞𝐰 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦'𝐬 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭𝐬 😇**\n\n**❓ 𝐅𝐨𝐫 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐀𝐛𝐨𝐮𝐭 𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞 𝐎𝐟 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭, 𝐉𝐮𝐬𝐭 𝐓𝐲𝐩𝐞 /cmdlist ".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", url="https://t.me/Miss_florence_bot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Rᴇᴘᴏ Sᴜᴘᴘᴏʀᴛ", url="https://t.me/SHIZUKA_VC_SUPPORT"),
            InlineKeyboardButton("📣 Oᴡɴᴇʀ Cʜᴀɴɴᴇʟ", url=f"https://t.me/aboutpratheek") 
            ],[
            InlineKeyboardButton("🥀 𝗗𝗘𝗩 ", url="https://t.me/pratheek06")
            ]]
        ),
        disable_web_page_preview=False
    )
        
@Client.on_message(filters.command(["start", "start@Miss_florence_bot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**𝑷𝒓𝒂𝒕𝒉𝒆𝒆𝒌 𝑴𝒖𝒔𝒊𝒄 𝑩𝒐𝒕 𝑰𝒔 𝑶𝒏𝒍𝒊𝒏𝒆 ✅**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🎙️ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣 🎙️", url="https://t.me/SHIZUKA_VC_SUPPORT")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@Miss_florence_bot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Miss_florence_bot : 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄**

__× 𝗙𝗜𝗥𝗦𝗧 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣..
× 𝗣𝗥𝗢𝗠𝗢𝗧𝗘 𝗠𝗘 𝗔𝗦 𝗔𝗗𝗠𝗜𝗡 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗪𝗜𝗧𝗛 𝗔𝗟𝗟 𝗣𝗘𝗥𝗠𝗜𝗦𝗦𝗜𝗢𝗡..__

**🏷 𝐂𝐨𝐦𝐦𝐨𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬.**

• `/play` <song name> - play song you requested
• `/playlist` - Show now playing list
• `/current` - Show now playing
• `/song` <song name> - download songs you want quickly
• `/search` <query> - search videos on youtube with details
• `/vid` <song name> - download videos you want quickly

**🏷 𝐆𝐫𝐨𝐮𝐩 𝐀𝐝𝐦𝐢𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬.**

• `/player` - open music player settings panel
• `/pause` - pause song play
• `/resume` - resume song play
• `/skip` - play next song
• `/end` - stop music play
• `/userbotjoin` - invite assistant to your chat
• `/userbotleave` - remove assistant from your chat
• `/reload` - Refresh admin list
: __ https:/t.me/aboutpratheek __""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣 🎙️", url="https://t.me/SHIZUKA_VC_SUPPORT")
              ]]
          )
      )
