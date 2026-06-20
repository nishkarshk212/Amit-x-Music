# Copyright (c) 2025 TheHamkerAlone 
# Licensed under the MIT License.
# This file is part of AmitMusic


import pyrogram

from Amit import config, logger


class Bot(pyrogram.Client):
    def __init__(self):
        super().__init__(
            name="Amit",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            parse_mode=pyrogram.enums.ParseMode.HTML,
            max_concurrent_transmissions=7,
            link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True),
        )
        self.owner = config.OWNER_ID
        self.logger = config.LOGGER_ID
        self.bl_users = pyrogram.filters.user()
        self.sudoers = pyrogram.filters.user(self.owner)

    async def boot(self):
        """
        Starts the bot and performs initial setup.
        """
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name
        self.username = self.me.username
        self.mention = self.me.mention

        logger.info(f"Trying to send startup message to LOGGER_ID={self.logger} (type: {type(self.logger)})")
        try:
            chat = await self.get_chat(self.logger)
            logger.info(f"Got chat info: {chat.id}, title={chat.title if hasattr(chat, 'title') else 'N/A'}")
            await self.send_message(self.logger, "🤖 Bot Started Successfully!\nUsername: @{}\nID: {}".format(self.username, self.id))
            get = await self.get_chat_member(self.logger, self.id)
            if get.status != pyrogram.enums.ChatMemberStatus.ADMINISTRATOR:
                logger.warning("Please promote the bot as an admin in logger group for full functionality.")
        except Exception as ex:
            logger.warning(f"Bot has failed to access the log group: {self.logger}\nReason: {type(ex)} - {ex}")
            import traceback
            logger.warning(f"Stack trace: {traceback.format_exc()}")
        logger.info(f"Bot started as @{self.username}")

    async def exit(self):
        """
        Asynchronously stops the bot.
        """
        await super().stop()
        logger.info("Bot stopped.")
