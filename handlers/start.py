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


@Client.on_message(filters.command(["start", "start@s4shiv_musicbot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="[ ](https://telegra.ph/file/0f8300efafe502f54efb4.mp4)**ððððð¢ ð§ððð¥ð â¥ï¸ {}!**\n\n**ðððð ðð ð ððððððð ððð ðð [ðððð](https://t.me/Shivamdemon)â¨.**\n\nð¶ ð¨ððððð ððð ð»ð ð·ððð ð´ðððð ð¶ð ð®ððððð ð»ðððððð ð»ðð ðµðð ð»ððððððð ð½ðððð ðªðððð\n\nð¥ð­ðð ð°ðððððððððð ð¨ðððð ð¨ðð ð­ðððððð ð¶ð ð»ððð ð©ðð, ðªðððð ð¶ð ð»ðð ðªððððððð â ð©ððððð ð©ðððð".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("â Sá´á´á´á´É´ Má´ â", url="https://t.me/S4shiv_musicBot?startgroup=true")
            ],[
            InlineKeyboardButton("ð¬ Sá´á´á´á´Êá´", url="https://t.me/Alone_boy_xd_01"),
            InlineKeyboardButton("ð£ Oá´¡É´á´Ê", url=f"https://t.me/Shivamdemon") 
            ],[
            InlineKeyboardButton("ð¥ ððð© ", url="https://t.me/shivamdemon")
            ],[
            InlineKeyboardButton("â ððððð", url="https://t.me/swagpartners_xd")
            ]]
        ),
        disable_web_page_preview=False
    )
        
@Client.on_message(filters.command(["start", "start@s4shiv_musicBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="ââDá´á´á´É´ Bá´á´ Is OÉ´ÊÉªÉ´á´ Ná´á´¡â",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="ðï¸ ð¦ð¨ð£ð£ð¢ð¥ð§ ðï¸", url="https://t.me/shivamdemon")
            ]]
        )
    )


@Client.on_message(filters.command(["phelp", "start@s4shiv_musicBot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**S4SHIV** : **HELP MENU**

__Ã ððð¥ð¦ð§ ððð ð ð ð§ð¢ ð¬ð¢ð¨ð¥ ðð¥ð¢ð¨ð£..
Ã ð£ð¥ð¢ð ð¢ð§ð ð ð ðð¦ ððð ðð¡ ðð¡ ð¬ð¢ð¨ð¥ ðð¥ð¢ð¨ð£ ðªðð§ð ððð ð£ðð¥ð ðð¦ð¦ðð¢ð¡..__

**ð· ðð¨ð¦ð¦ð¨ð§ ðð¨ð¦ð¦ðð§ðð¬.**

â¢ `/play` <song name> - play song you requested
â¢ `/playlist` - Show now playing list
â¢ `/current` - Show now playing
â¢ `/song` <song name> - download songs you want quickly
â¢ `/search` <query> - search videos on youtube with details
â¢ `/vid` <song name> - download videos you want quickly

**ð· ðð«ð¨ð®ð© ððð¦ð¢ð§ ðð¨ð¦ð¦ðð§ðð¬.**

â¢ `/player` - open music player settings panel
â¢ `/pause` - pause song play
â¢ `/resume` - resume song play
â¢ `/skip` - play next song
â¢ `/end` - stop music play
â¢ `/userbotjoin` - invite assistant to your chat
â¢ `/userbotleave` - remove assistant from your chat
â¢ `/reload` - Refresh admin list
 __ SÊÉªá´ ð¥ __""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="ðï¸ ð¦ð¨ð£ð£ð¢ð¥ð§  ðï¸", url="https://t.me/SHIVAMDEMON")
              ]]
          )
      )


@Client.on_message(filters.command(["ping", "ping@S4SHIV_MUSICBot"]) & ~filters.edited)
async def ping_pong(_, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "ð¥ `PONG!!`\n"
        f"â¡ï¸ `{delta_ping * 1000:.3f} ms`",
    )


@Client.on_message(filters.command(["uptime", "uptime@Aturma_Vc_Bot"]) & ~filters.edited)
async def get_uptime(_, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "ð¤ bot status:\n"
        f"â¢ **uptime:** `{uptime}`\n"
        f"â¢ **start time:** `{START_TIME_ISO}`",
    )
