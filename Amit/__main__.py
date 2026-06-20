# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of AmitMusic


import asyncio
import importlib

from pyrogram import idle

from Amit import (anon, app, config, db,
                   logger, stop, userbot, yt)
from Amit.plugins import all_modules


async def main():
    await db.connect()
    await app.boot()
    
    try:
        await userbot.boot()
    except Exception as ex:
        import traceback
        logger.warning(f"Userbot failed to start: {type(ex)} {ex}")
        logger.warning(f"Stack trace:\n{traceback.format_exc()}")
    
    await anon.boot()

    for module in all_modules:
        importlib.import_module(f"Amit.plugins.{module}")
    logger.info(f"Loaded {len(all_modules)} modules.")

    if config.COOKIES_URL:
        await yt.save_cookies(config.COOKIES_URL)

    sudoers = await db.get_sudoers()
    app.sudoers.update(sudoers)
    app.bl_users.update(await db.get_blacklisted())
    logger.info(f"Loaded {len(app.sudoers)} sudo users.")

    await idle()
    await stop()


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        pass
