from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["start", "start@Aturma_Vc_Bot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="[ ](https://telegra.ph/file/ba834db90aa69f8b17b31.mp4)**𝗛𝗘𝗟𝗟𝗢 𝗧𝗛𝗘𝗥𝗘 ♥️ {}!**\n\n**𝐓𝐇𝐈𝐒 𝐈𝐒 𝐀 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐁𝐎𝐓 𝐎𝐅 𝐏𝐑𝐀𝐓𝐇𝐄𝐄𝐊✨.**\n\n🎶 𝑨𝒍𝒍𝒐𝒘𝒔 𝒀𝒐𝒖 𝑻𝒐 𝑷𝒍𝒂𝒚 𝑴𝒖𝒔𝒊𝒄 𝑶𝒏 𝑮𝒓𝒐𝒖𝒑𝒔 𝑻𝒉𝒓𝒐𝒖𝒈𝒉 𝑻𝒉𝒆 𝑵𝒆𝒘 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕𝒔\n\n🥀𝑭𝒐𝒓 𝑰𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 𝑨𝒃𝒐𝒖𝒕 𝑨𝒍𝒍 𝑭𝒆𝒂𝒕𝒖𝒓𝒆 𝑶𝒇 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕, 𝑪𝒍𝒊𝒄𝒌 𝑶𝒏 𝑻𝒉𝒆 𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 ⚙ 𝑩𝒖𝒕𝒕𝒐𝒏 𝑩𝒆𝒍𝒐𝒘".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Sᴜᴍᴍᴏɴ Mᴇ ➕", url="https://t.me/Aturma_Vc_Bot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Rᴇᴘᴏ Sᴜᴘᴘᴏʀᴛ", url="https://t.me/SHIZUKA_VC_SUPPORT"),
            InlineKeyboardButton("📣 Oᴡɴᴇʀ Cʜᴀɴɴᴇʟ", url=f"https://t.me/aboutpratheek") 
            ],[
            InlineKeyboardButton("🥀 𝗗𝗘𝗩 ", url="https://t.me/pratheek06")
            ],[
            InlineKeyboardButton("⚙ Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/HOW-TO-USE-PRATHEEK-PRIVATE-MUSIC-BOT-09-24-2")
            ]]
        ),
        disable_web_page_preview=False
    )
        
@Client.on_message(filters.command(["start", "start@Aturma_Vc_Bot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="✅★Pʀᴀᴛʜᴇᴇᴋ Bᴏᴛ Is Oɴʟɪɴᴇ Nᴏᴡ★",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🎙️ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣 🎙️", url="https://t.me/SHIZUKA_VC_SUPPORT")
            ]]
        )
    )


@Client.on_message(filters.command(["phelp", "start@Aturma_Vc_Bot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**PRATHEEK_XD** : **HELP MENU**

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
 __ Pʀᴀᴛʜᴇᴇᴋ 🥀 __""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣 🎙️", url="https://t.me/SHIZUKA_VC_SUPPORT")
              ]]
          )
      )


@Client.on_message(filters.command(["ping", "ping@Aturma_Vc_Bot"]) & ~filters.edited)
async def ping_pong(_, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`",
    )


@Client.on_message(filters.command(["uptime", "uptime@Aturma_Vc_Bot"]) & ~filters.edited)
async def get_uptime(_, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`",
    )
