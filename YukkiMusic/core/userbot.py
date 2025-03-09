import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot:
    def __init__(self):
        self.one = self.create_client(config.STRING1) if config.STRING1 else None
        self.two = self.create_client(config.STRING2) if config.STRING2 else None
        self.three = self.create_client(config.STRING3) if config.STRING3 else None
        self.four = self.create_client(config.STRING4) if config.STRING4 else None
        self.five = self.create_client(config.STRING5) if config.STRING5 else None

    def create_client(self, session_string):
        return Client(
            name="assistant",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=session_string,  # FIXED: Changed from session_name
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("Starting Assistant Clients")

        for idx, client in enumerate([self.one, self.two, self.three, self.four, self.five], start=1):
            if client:
                await self.start_client(client, idx)

    async def start_client(self, client, index):
        await client.start()
        try:
            await client.join_chat("TeamYM")
            await client.join_chat("TheYukki")
            await client.join_chat("YukkiSupport")
        except:
            pass

        assistants.append(index)
        try:
            await client.send_message(config.LOG_GROUP_ID, "Assistant Started")
        except:
            LOGGER(__name__).error(
                f"Assistant Account {index} failed to access log group. Add and promote it as an admin!"
            )
            sys.exit()

        get_me = await client.get_me()
        client.username = get_me.username
        client.id = get_me.id
        assistantids.append(get_me.id)
        client.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name

        LOGGER(__name__).info(f"Assistant {index} started as {client.name}")
