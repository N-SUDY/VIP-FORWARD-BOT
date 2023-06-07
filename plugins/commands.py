import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import sys
from Script import script



buttons=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Help 🍁", callback_data="help"),
                InlineKeyboardButton("About 🍃", callback_data="abt")
            ],
            [
                InlineKeyboardButton("Source Code 🧑‍💻", url="https://github.com/ritesh-0/public-forward-bot"),
                InlineKeyboardButton("Updates Channel 📢", url="https://t.me/+yYhfz5JwILhmODc9")
            ]
        ]
        )

back_btn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back", callback_data="backabt")
            ]
        ]   
    )

@Client.on_message(filters.private & filters.command('start'))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=script.START_TXT.format(
                message.from_user.first_name),
        reply_markup=buttons,
        parse_mode="html")


@Client.on_message(filters.command("stop"))
async def stop_button(bot, message):

    if str(message.from_user.id) not in Config.OWNER_ID:
        return
    msg = await bot.send_message(
        text="Stoping all processes...",
        chat_id=message.chat.id
    )
    await asyncio.sleep(1)
    await msg.edit("All Processes Stopped and Restarted")
    os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_message(filters.private & filters.command('help'))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=script.HELP_TXT,
        parse_mode="html")


@Client.on_callback_query(filters.regex(r'^help$'))
async def cb_help(bot, cb):
    await cb.message.edit_text(script.HELP_TXT, reply_markup=back_btn)



@Client.on_callback_query(filters.regex(r'^abt$'))   
async def cb_abt(bot, cb):
    await cb.message.edit_text(script.ABOUT_TXT,
    disable_web_page_preview = True,    
    reply_markup= back_btn
    )


@Client.on_callback_query(filters.regex(r'^backabt$'))
async def cb_back_abt(bot, cb):
    await cb.message.edit_text(script.START_TXT.format(cb.from_user.first_name), reply_markup= buttons)


@Client.on_callback_query(filters.regex(r'^backabt$'))
async def cb_back_help(bot, cb):
    await cb.message.edit_text(script.START_TXT.format(cb.from_user.first_name), reply_markup= buttons)
