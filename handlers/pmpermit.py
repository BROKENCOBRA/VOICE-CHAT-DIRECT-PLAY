from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"[ ](https://telegra.ph/file/68b4fedada212036e846b.jpg) 𝑯𝒆𝒍𝒍𝒐 𝑻𝒉𝒆𝒓𝒆𐂃...♥️\n𝑰𝒂𝒎 𝑨 𝑷𝒓𝒊𝒗𝒂𝒕𝒆 𝑴𝒖𝒔𝒊𝒄 𝑩𝒐𝒕 𝑶𝒇 𝑷𝒓𝒂𝒕𝒉𝒆𝒆𝒌 ♫︎ 🥀\n\n➖ 𝚂𝙾𝚁𝚁𝚈 𝙸𝙵 𝙸 𝚆𝙾𝙽𝚃 𝚁𝙴𝙿𝙻𝚈 𝚈𝙾𝚄.. 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙶𝚁𝙾𝚄𝙿 𝙻𝙸𝙽𝙺 𝙷𝙴𝚁𝙴 𝙾𝚁 𝙹𝙾𝙸𝙽 @SHIZUKA_VC_SUPPORT 𝙰𝙽𝙳 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙰𝙳𝙼𝙸𝙽 𝙷𝙴𝚁𝙴 \n\n▪️𝒂𝒏𝒚 𝒊𝒔𝒔𝒖𝒆𝒔 : @pratheek06 \n▪️𝒋𝒐𝒊𝒏 𝒉𝒆𝒓𝒆 : @ABOUTPRATHEEK \n\n") 
  return


@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("✅ approved to pm.")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("❌ disapproved to pm.")
        return
    message.continue_propagation()
