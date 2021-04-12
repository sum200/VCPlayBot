from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAx0CTf99nAACCK9gdKpBPyZVogv20bYuxP9I8OO_lwACxAEAArzunx4JdkJmhvq8Vh4E")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI'm Rythm i can play music in your group's voice chat.
\n🎵🎵🎶🎵🎵.
\nUse the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Music World", url="https://t.me/RythmMusic",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/RythmMusic"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/RythmMusic"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/QueenArzoo/VCPlayBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/EmilyVCBot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
