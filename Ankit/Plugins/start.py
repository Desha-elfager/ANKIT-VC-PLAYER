import asyncio
from time import time
from datetime import datetime
from Ankit import BOT_USERNAME
from Ankit.config import UPDATES_CHANNEL, ANKIT_SUPPORT
from Ankit.MusicUtilities.helpers.filters import command
from Ankit.MusicUtilities.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


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
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6409c1160ffcae173900f.jpg",
        caption=f"""**A Telegram Music Bot Based Mongodb.
 Add Me To Ur Chat For and Help and And Support Click On Buttons  ...
Powered By [©LEGEND-ANKIT™](https://github.com/LEGEND-ANKIT) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰 ©LEGEND-ANKIT™ 🔰", url=f"https://github.com/LEGEND-ANKIT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰 DEVELOPER ↗", url=f"https://github.com/LEGEND-ANKIT"
                    ),
                    InlineKeyboardButton(
                        "🔰 CREATOR ↗", url="https://github.com/LEGEND-ANKIT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔰 SUPPORT CHANNEL ↗", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "🔰 SUPPORT GROUP ↗", url=f"https://t.me/{ANKIT_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6409c1160ffcae173900f.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 SUPPORT GROUP 💞", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(command(["ankit", "owner"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6409c1160ffcae173900f.jpg",
        caption=f"""Here Is The Ankit Github Account✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰©ANKIT™🔰", url=f"https://telegra.ph/file/6409c1160ffcae173900f.jpg")
                ]
            ]
        ),
    )
