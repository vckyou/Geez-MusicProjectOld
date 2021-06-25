# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  VckyouuBitch
# Recode By VICKY From Geez-MusicProject

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from asyncio.queues import QueueEmpty
from GeezProject.config import que
from pyrogram import Client, filters
from pyrogram.types import Message
import sira
import tgcalls
from GeezProject.function.admins import set
from GeezProject.helpers.channelmusic import get_chat_id
from GeezProject.helpers.decorators import authorized_users_only, errors
from GeezProject.helpers.filters import command, other_filters
from GeezProject.services.callsmusic import callsmusic


@Client.on_message(filters.command("adminreset"))
async def update_admin(client, message: Message):
    chat_id = get_chat_id(message.chat)
    set(
        chat_id,
        (
            member.user
            for member in await message.chat.get_members(
                filter="administrators"
            )
        ),
    )

    await message.reply_text("✅️ Admin cache refreshed!")


@Client.on_message(command(["pause", "jeda"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    callsmusic.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("⏸ Music Di Hentikan Sementara.")


@Client.on_message(command(["resume", "lanjut"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("▶️ Music Dilanjut.")


@Client.on_message(command(["end", "stop"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
       callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
       pass

    callsmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("❌ **Menghentikan Lagu!**")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)

    callsmusic.queues.task_done(message.chat.id)
    await message.reply_text("⏩ Melanjut Ke Antrian Selanjutnya.")
    if callsmusic.queues.is_empty(message.chat.id):
        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("Music Dihentikan, Antrian Tidak Terdeteksi")
    else:
        callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )

        await message.reply_text(" ")


@Client.on_message(filters.command("admincache"))
@errors
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(
                filter="administrators"
            )
        ),
    )

    await message.reply_text("✅️ **Daftar admin** telah **diperbarui**")
