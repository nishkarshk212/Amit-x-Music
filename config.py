#ALONE CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "17596251"))
        self.API_HASH = getenv("API_HASH", "e58343b4c0193e293e391daf97603fcd")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "Apna Bot Token")
        self.MONGO_URL = getenv("MONGO_URL", "Apna Mongo Db Dalo")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "Apna Log Group Id Dalo"))
        self.OWNER_ID = int(getenv("OWNER_ID", "Owner I'd dalo"))
        
        self.SESSION1 = getenv("SESSION", "Apna String Dalo")
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
        self.YT_API_KEY = getenv("YT_API_KEY", None)
        self.YTPROXY_URL = getenv("YTPROXY_URL", None)
        self.ARU_API_KEY = getenv("ARU_API_KEY", None)
        self.ARU_API_URL = getenv("ARU_API_URL", None)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://i.ibb.co/WppbqXQn/cat-clouds-looking-stars.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://i.ibb.co/Qjn7y0qp/anime-style-animal-digital-art.jpg")
        self.START_IMG = getenv("START_IMG", "https://i.ibb.co/n80Z3Mx3/medium-shot-anime-woman-hugging-cat.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
