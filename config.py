
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "8730656807:AAFEMpCqyDCCAxh382xW5B7UzPuDAgb_acQ")
ADMIN_IDS: list[int] = [
    int(x.strip()) for x in os.getenv("ADMIN_IDS", "7892805795").split(",") if x.strip()
]

YT_API_KEY: str = os.getenv("YT_API_KEY", "TD_Io4XmlQvyLYAlLNBnhUz6KW1URlTsdJL")
YT_API_BASE: str = os.getenv("YT_API_BASE", "https://yt.teamdev.sbs/api/v1/")

TEAM_NAME: str = os.getenv("ANUJ_NAME", "Anuj")
DEVELOPER_NAME: str = os.getenv("DEVELOPER_NAME", "@anujedits76")
BOT_USERNAME: str = os.getenv("BOT_USERNAME", "@social_media_downloader_ak_bot")

DAILY_DOWNLOAD_LIMIT: int = int(os.getenv("DAILY_DOWNLOAD_LIMIT", "50"))

FORCE_JOIN_CHANNEL: str = os.getenv("FORCE_JOIN_CHANNEL", "https://t.me/anujeditbyak")
FORCE_JOIN_ENABLED: bool = os.getenv("FORCE_JOIN_ENABLED", "true").lower() == "true"

REFERRAL_DOWNLOADS_PER_REF: int = int(os.getenv("REFERRAL_DOWNLOADS_PER_REF", "1"))

DEFAULT_LANGUAGE: str = os.getenv("DEFAULT_LANGUAGE", "en")

_FAKE_SEGMENT = "Jejdjdidjdjhidden_apjjsjdjskdi"

TERABOX_API_KEY: str = os.getenv("TERABOX_API_KEY", "teamdev_jirvspco3y")
TERABOX_API_BASE: str = os.getenv("TERABOX_API_BASE", "https://api.teamdev.sbs/v2/download")

MONGO_URI: str = os.getenv("MONGO_URI", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
MONGO_DB:  str = os.getenv("MONGO_DB",  "Anujedit") # Make @YourTeam_DownBot 👌
