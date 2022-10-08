import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("/start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 مرحبا انا بوت يمكنني تشغيل الاغاني في المكالمات الصوتيه
اضغط على زر الاوامر لمعرفة طريقة التشغيل 
قناة ســـورس روسيا 🇷🇺 [قناة السورس](https://t.me/X_x_RUSSIA_x_X)...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اضفني لي مجموعتك ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        " ⚙️ ¦ السورس ", url=f"https://t.me/X_x_RUSSIA_x_X"
                    ),
                    InlineKeyboardButton(
                        " ☣️ ¦ جـروب الدعم ", url=f"https://t.me/RUSSIA_TEST}"
                    )
                ],[
                    InlineKeyboardButton(
                        " 🖥 ¦ الأوامــر ", url=f"https://telegra.ph/%F0%9D%91%BA%F0%9D%91%BC%F0%9D%91%B6%F0%9D%91%B9%F0%9D%91%AA%F0%9D%91%AC-%F0%9D%91%A9%F0%9D%91%AC%F0%9D%91%B4%F0%9D%91%A9%F0%9D%91%B6-06-190%9D%91%B6-06-19"
                    ),
                    InlineKeyboardButton(
                        " 🧨 ¦ مطور السورس ", url="https://t.me/@DEV_EL_ZOOZE"
                    )]
            ]
       ),
    )

@Client.on_message(command(["مبرمج السورس","سورس" ,"السورس"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2d1372d13b7b8f496b0d1.jpg",
        caption=f""" [⍟ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚐𝚘𝚍𝚣𝚎𝚕ł𝚊](https://t.me/X_x_RUSSIA_x_X)  """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton(" ᯓ 𓆩 ˹ 𝑅𝐔𝑆𝑆𝐼𝐴𝑆𝑂𝐔𝑅𝐶𝐸 ˼ 𓆪 𓆃", url=f"https://t.me/R7SH0"),
           ],
            [ 
                InlineKeyboardButton(" ᯓ 𓆩 ˹ 𝐂𝐇𝐀𝐍𝐍𝐄𝑳 ˼ 𓆪 𓆃", url=f"https://t.me/RUSSIA_HELP_SOURSE"),
            ],
            [
                InlineKeyboardButton(
                    " ᯓ 𓆩 ˹ 𝐂𝐇 𝐒𝐎𝐔𝐑𝐂𝐄 ˼ 𓆪 𓆃", url=f"https://t.me/X_x_RUSSIA_x_X"
                ),
            ],
            [
                InlineKeyboardButton("🐥اضفني الى مجموعتك🐥", url=f"https://t.me/K61TBot?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["المطور", "/godzela", "مطور" ,"مطور البوت"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/030a9f0a9604949388a16.jpg",
        caption=f""" الاول: هو مطور السورس🐥 \n الثاني: مطور البوت🐥 \n√""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton(" ᯓ 𓆩 ˹ 𝑅𝐔𝑆𝑆𝐼𝐴𝑆𝑂𝐔𝑅𝐶𝐸 ˼ 𓆪 𓆃", url=f"https://t.me/X_x_RUSSIA_x_X"),
            ],
            [
                InlineKeyboardButton(
                        DEV_RUSSIA, url=f"https://t.me/DEV_EL_ZOOZE"
                ),
            ],
            [
                InlineKeyboardButton("🐥ضيـف البـوت لمجمـوعتـك🐥", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "🐥 **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                "🐥 **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم او روسيا تعاله` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⚙️ ¦ السورس ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("☣️ ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "🐥اضـفني لي مـجـمـوعـتـك🐥",
                        url=f'https://t.me/K61TBot?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
