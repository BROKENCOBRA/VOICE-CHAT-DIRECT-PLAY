from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"[𝐒𝐇𝐈𝐕](https://t.me/shivamdemon) 𝑯𝒆𝒍𝒍𝒐 𝑻𝒉𝒆𝒓𝒆𐂃...♥️\n𝑰𝒂𝒎 𝑨 𝑷𝒓𝒊𝒗𝒂𝒕𝒆 𝑴𝒖𝒔𝒊𝒄 𝑩𝒐𝒕 𝑶𝒇 𝑺𝒉𝒊𝒗 ♫︎ 🥀\n\n➖ 𝚂𝙾𝚁𝚁𝚈 𝙸𝙵 𝙸 𝚆𝙾𝙽𝚃 𝚁𝙴𝙿𝙻𝚈 𝚈𝙾𝚄.. 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙶𝚁𝙾𝚄𝙿 𝙻𝙸𝙽𝙺 𝙷𝙴𝚁𝙴 𝙾𝚁 𝙲𝙷𝙰𝚃 @SHIVAMDEMON 𝙰𝙽𝙳 𝙲𝙾𝙽𝚃𝙰𝙲𝚃  𝙷𝙴𝚁𝙴 \n\n▪️𝒂𝒏𝒚 𝒊𝒔𝒔𝒖𝒆𝒔 : @shivamdemon \n▪️𝑨𝒅𝒅 𝒃𝒐𝒕 : @S4shiv_musicbot \n\n") 
  return
