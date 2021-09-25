import sys
import os
import time
import traceback
import asyncio
import shutil
import psutil

# Stats Of Your Bot
@Client.on_message(filters.command("stats"))
@sudo_users_only
async def botstats(_, message: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await message.reply_text(
        text=f"**📊 stats Of @{BOT_USERNAME}** \n\n**🤖 bot version:** `v6.5` \n\n**🙎🏼 users:** \n » **users on pm:** `{total_users}` \n\n**💾 disk usage,** \n » **disk space:** `{total}` \n » **used:** `{used}({disk_usage}%)` \n » **free:** `{free}` \n\n**🎛 hardware usage,** \n » **CPU usage:** `{cpu_usage}%` \n » **RAM usage:** `{ram_usage}%`",
        parse_mode="Markdown",
        quote=True
    )
