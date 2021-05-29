from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from GeezProject.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("BROADCAST!!!")
        if not message.reply_to_message:
            await lol.edit("`MOHON BALAS KEPESAN UNTUK MELAKUKAN BROADCAST`")
            return
        msg = message.reply_to_message.text
        for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"BROADCAST.. Terkirim: {sent} Chats. GAGAL MENGIRIM : {failed} Chats.")
            except:
                failed=failed+1
                await lol.edit(f"BROADCAST.. Terkirim: {sent} chats. GAGAL MENGIRIM: {failed} Chats.")
            await asyncio.sleep(0.7)
        await message.reply_text(f"MENGIRIM BROADCAST KE {sent} Chats. GAGAL MENGIRIM: {failed} Chats.")
