#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot:
    def __init__(self):
        self.one = Client(
            name="assistant_1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        ) if config.STRING1 else None

        self.two = Client(
            name="assistant_2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        ) if config.STRING2 else None

        self.three = Client(
            name="assistant_3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        ) if config.STRING3 else None

        self.four = Client(
            name="assistant_4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        ) if config.STRING4 else None

        self.five = Client(
            name="assistant_5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        ) if config.STRING5 else None

    async def start(self):
        LOGGER(__name__).info("Starting Assistant Clients")

        for idx, assistant in enumerate([self.one, self.two, self.three, self.four, self.five], start=1):
            if assistant:
                await assistant.start()
                try:
                    await assistant.join_chat("TeamYM")
                    await assistant.join_chat("TheYukki")
                    await assistant.join_chat("YukkiSupport")
                except:
                    pass

                assistants.append(idx)

                try:
                    await assistant.send_message(config.LOG_GROUP_ID, "Assistant Started")
                except:
                    LOGGER(__name__).error(
                        f"Assistant Account {idx} failed to access log group. Make sure the assistant is added and promoted as admin!"
                    )
                    sys.exit()

                get_me = await assistant.get_me()
                assistant.username = get_me.username
                assistant.id = get_me.id
                assistantids.append(get_me.id)
                assistant.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name

                LOGGER(__name__).info(f"Assistant {idx} Started as {assistant.name}")
