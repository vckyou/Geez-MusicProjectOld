# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# recode by levina-lab on github
# originally rewritten by using existing code (fixed)

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from GeezProject.services.callsmusic.callsmusic import client as geez
from GeezProject.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`memulai global cast...`")
        if not message.reply_to_message:
            await wtf.edit("balas ke pesan untuk melakukan broadcast!")
            return
        lmao = message.reply_to_message.text
        async for dialog in geez.iter_dialogs():
            try:
                await geez.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`global cast...` \n\n**mengirim ke:** `{sent}` obrolan \n**gagal di:** {failed} obrolan")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`gcast berhasil` \n\n**terkirim ke:** `{sent}` obrolan \n**gagal di:** {failed} obrolan")
