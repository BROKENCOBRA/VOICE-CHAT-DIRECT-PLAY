from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@MemoriesMusicBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello 👋🏻 {}!**\n\nI **Can Play Music In Voice Chats of Telegram Groups.**I Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Usage ❤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ 𝙰𝙳𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ➕", url="https://t.me/MemoriesMusicBot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 𝙶𝚁𝙾𝚄𝙿", url="https://t.me/Team_Memories_Support"),
            InlineKeyboardButton("📣 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/Team_Memories") 
            ],[
            InlineKeyboardButton("😈 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 ", url="https://t.me/Memory_XY")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@MemoriesMusicBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**𝙼𝙴𝙼𝙾𝚁𝙸𝙴𝚂 𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴 ✅**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/Team_Memories_Support")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@MemoriesMusicBot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**𝙼𝙴𝙼𝙾𝚁𝙸𝙴𝚂 𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃 : 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄**

__× 𝙵𝙸𝚁𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿..
× 𝙿𝚁𝙾𝙼𝙾𝚃𝙴 𝙼𝙴 𝙰𝚂 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝚆𝙸𝚃𝙷 𝙰𝙻𝙻 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽..__

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
 : __https:/t.me/Team_Memories__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/Team_Memories_Support")
              ]]
          )
      )
