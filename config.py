#ALONE CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "17596251"))
        self.API_HASH = getenv("API_HASH", "e58343b4c0193e293e391daf97603fcd")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "6808170222:AAEN4RaxQGJMVFEcQwyaskvQ-qXdxY2p34A")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://bhulud30_db_user:bhulud30_db_user@cluster0.yzspcrl.mongodb.net/?appName=Cluster0")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003809958673"))
        self.OWNER_ID = int(getenv("OWNER_ID", "8458947967"))
        
        self.SESSION1 = getenv("SESSION", "BQCZzqEAUikUU0qF6HUdl0ak3UBNyhdQ7tFKe0GRRrUUTT5c2EWUq-JI_E10vQZvc5LckyYCxXfBmjC6l7sFlRQTSKTVs0yQue2Y-4HH-GgVs3wDPctYZ2PHTq1LuBgqJ_WCOuPPvPRpTdCtUVecTDHAkCTobfWZDGRmQpEIuo3y8fFttnQ9G1nbQfQPbuyorqTKlyWudjwCd61OrKytYmI7D0eNwkfuSU0CqbIEbYyfoZvqBHH9XhU0jQ3FS99aLFBd6U8SnVN106MlIEDYTqH9JCNoDSMbplDZGmRCyQcxjoe7lJHlJAMbUXZc2HdXaFlhq2KU2WltrrCgmivzOKZSeWZsKQAAAAH2m3NPAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneUpdates")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AloneBotSupport")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY", "INFLEX68575028D")
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
