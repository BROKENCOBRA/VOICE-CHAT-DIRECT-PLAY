from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"[ππππ](https://t.me/shivamdemon) π―ππππ π»πππππ...β₯οΈ\nπ°ππ π¨ π·ππππππ π΄ππππ π©ππ πΆπ πΊπππ β«οΈ π₯\n\nβ ππΎπππ πΈπ΅ πΈ ππΎπ½π ππ΄πΏπ»π ππΎπ.. πΉπππ ππ΄π½π³ πΌπ΄ πΆππΎππΏ π»πΈπ½πΊ π·π΄ππ΄ πΎπ π²π·π°π @SHIVAMDEMON π°π½π³ π²πΎπ½ππ°π²π  π·π΄ππ΄ \n\nβͺοΈπππ ππππππ : @shivamdemon \nβͺοΈπ¨ππ πππ : @S4shiv_musicbot \n\n") 
  return
