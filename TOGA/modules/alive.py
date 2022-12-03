import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from TOGA.events import register
from TOGA import telethn as tbot


PHOTO = "https://telegra.ph/file/d3f99f09b19779a65017b.jpg"

@register(pattern=("/alive"))
async def awake(event):
  text2 = f"**Heyaa.. Weeb! [{event.sender.first_name}](tg://user?id={event.sender.id}), I'M Himiko Toga.** \n\n"
  text2 += "⁜ **I'll Be Giving My Best For Your Work !!** \n\n"
  text2 += f"⁜ **Library Version :** `{telever}` \n\n"
  text2 += f"⁜ **Telethon Version :** `{tlhver}` \n\n"
  text2 += f"⁜ **Pyrogram Version :** `{pyrover}` \n\n"
  text2 += "**⁜Thanks For Adding Me Here ⁜**"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/TOGAUPDATES"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/TOGASUPPORT")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=text2,  buttons=BUTTON)
