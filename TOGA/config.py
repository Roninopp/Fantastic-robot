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
    BOT_API_URL="5614075230:AAHwMlH22eJH8BgVDyHTI0bPWODMRu727pI"
    #kacrmdi
    WOLVES=[5163444566]
    BOT_ID="5614075230" 
    SQLALCHEMY_DATABASE_URI="postgres://egrrjbpz:cXiNSVqvu3p-mYLFa_BI6M2UZfca1Akl@lallah.db.elephantsql.com/egrrjbpz" 
    JOIN_LOGGER="-1001745971242" 
    API_HASH="858d65155253af8632221240c535c314" 
    INFOPIC=True
    TIGERS=[5163444566]
    API_ID="26788480"
    BL_CHATS=[1]
    DB_URL2="egrrjbpz" 
    TOKEN="5614075230:AAHwMlH22eJH8BgVDyHTI0bPWODMRu727pI"
    DEV_USERS=[5163444566]
    DRAGONS=[5163444566]
    SPAMWATCH_API=""
    WALL_API=""
    DEMONS=[5163444566]
    SUPPORT_CHAT="TogaSupport"
    OWNER_USERNAME="PervertSenpai"
    DONATION_LINK="lwdaalay"
    EVENT_LOGS="-1001745971242" 
    OWNER_ID="5163444566" 
    TIME_API_KEY=""
    ERROR_LOGS="-1001745971242" 
    BOT_NAME="toga_robot"
    STRICT_GBAN=True
    REDIS_URL="redis://betatoga:Betatoga123+@redis-15793.c241.us-east-1-4.ec2.cloud.redislabs.com:15793"
    UPDATE_CHANNEL="TogaUpdates"
    MONGO_DB_URI="mongodb+srv://betatoga:Betatoga123+@betatoga.rrk13ss.mongodb.net/?retryWrites=true&w=majority"
    BOT_USERNAME="Toga_Robot"
    REM_BG_API_KEY=""
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID="-1001745971242"
    STRICT_GMUTE=False
    SPAMWATCH_API=""
    OWNER_NAME="KACCHAN"
    BANCODES=""
    REPOSITORY="GitHub.com/kac-chan/toga"
    ARQ_API_KEY=""
    ARQ_API_URL=""
    COTB=""

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
