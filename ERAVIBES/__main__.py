#
# Copyright (C) 2024 by amritraj78@Github, < https://github.com/amritraj78 >.
#
# This file is part of < https://github.com/amritraj78/ANIME-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/amritraj78/ANIME-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from ERAVIBES import HELPABLE, LOGGER, app, userbot
from ERAVIBES.core.call import ERA
from ERAVIBES.plugins import ALL_MODULES
from ERAVIBES.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("ERAVIBES").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("ERAVIBES").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("ERAVIBES.plugins").info("Successfully Imported All Modules ")

    await userbot.start()
    await ERA.start()
    await ERA.decorators()
    LOGGER("ERAVIBES").info("ERAVIBES STARTED SUCCESSFULLY 🕊️")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("ERAVIBES").info("Stopping ERAVIBES! GoodBye")
