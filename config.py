# Regen & Mod by @shamilhabeebnelli
# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "http://node-25.zeno.fm/kezsc0y2wwzuv?listening-from-radio-garden=1622271954020&rj-ttl=5&rj-tok=AAABec5bAE4Aj31dmRAEFgcbvw")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '1197404093')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '7073300'))
    CHAT = int(os.environ.get("CHAT", "1215554399"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "Y")
    ARQ_API=os.environ.get("ARQ_API", "LSLHIL-HGARDP-PLIXOB-CKHZEO-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    DURATION_LIMIT=int(os.environ.get("DUR", 15))
    API_HASH = os.environ.get("API_HASH", "7fc8f6ec7a39ba84b6b0162369b047ad")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1848759153:AAFWIIxE3siLXVwcODp9HGuJzkmnW6jlSrQ") 
    SESSION = os.environ.get("SESSION_STRING", "AQAdNlfoA4BYfNseeQcAqnLeXX72CR0W_vClGDdLfTCz7vD39fsyI7Y92Z-M25h8hPfSUtfnXvmA91XeiwhHDpWrghCsa3VN0bxw30Q1aZ-V3myJLeUNJqmarK75cAPusOUSY9knKBFCVN3CBSKP4GYfabT5jAWa6g93zMn4jC157AiC7ftS-BQyipszgpclx7QQmUy1NfTAn6SFeQQzMa7V6ziKtwLXn4y4lAm-SAJqMQMUU8rBbm2WOwEwBqU-OxDm8NbFDuuIDuJ2ir--1AhBkeLQJHxn7q3n02XtAYxjQujcBM8VyiDP2z02FWsUQtS0Da9YmarEFE-24bSq9RheR17vvQA")
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    playlist=[]
    msg = {}
