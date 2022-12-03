import json
import os


def get_user_list(config, key):
    with open('{}/TOGA/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER=True
    URL=False
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY=""
    DEL_CMDS=False
    BAN_STICKER=""
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB=""
    WEBHOOK=False
    BOT_API_URL=""
    #kacrmdi
    WOLVES=[]
    BOT_ID="" 
    SQLALCHEMY_DATABASE_URI="" 
    JOIN_LOGGER="" 
    API_HASH="" 
    INFOPIC=True
    TIGERS=[]
    API_ID=""
    BL_CHATS=[1]
    DB_URL2="" 
    TOKEN=""
    DEV_USERS=[]
    DRAGONS=[]
    SPAMWATCH_API=""
    WALL_API=""
    DEMONS=[]
    SUPPORT_CHAT="TogaSupport"
    OWNER_USERNAME=""
    DONATION_LINK=""
    EVENT_LOGS="" 
    OWNER_ID="" 
    TIME_API_KEY=""
    ERROR_LOGS="" 
    BOT_NAME="toga_robot"
    STRICT_GBAN=True
    REDIS_URL=""
    UPDATE_CHANNEL="TogaUpdates"
    MONGO_DB_URI=""
    BOT_USERNAME="Toga_Robot"
    REM_BG_API_KEY=""
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID=""
    STRICT_GMUTE=False
    AFKVID=""
    GROUP_ALIVE_PIC=""
    SPAMWATCH_API=""
    OWNER_NAME = ""
    BANCODES = ""
    REPOSITORY = "GitHub.com/kac-chan/toga"
    RED7_TOKEN = ""

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
