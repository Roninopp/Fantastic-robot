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
    BOT_API_URL="5696500136:AAF_i0YIrihTkovpuMUroZLNLnO5S5H90J0"
    #kacrmdi
    WOLVES=[5163444566]
    BOT_ID="5696500136" 
    SQLALCHEMY_DATABASE_URI="postgresql://hrtmlhvm:KlLKwbOBV7kRzJNDQbigew0eA1N_2qEf@castor.db.elephantsql.com/hrtmlhvm" 
    JOIN_LOGGER="-1001745971242" 
    API_HASH="c1b434defccacad6063758c9a7d76d5d" 
    INFOPIC=True
    TIGERS=[5163444566]
    API_ID="13849191"
    BL_CHATS=[1]
    DB_URL2="egrrjbpz" 
    TOKEN="5696500136:AAF_i0YIrihTkovpuMUroZLNLnO5S5H90J0"
    DEV_USERS=[5163444566]
    DRAGONS=[5163444566]
    SPAMWATCH_API=""
    WALL_API=""
    DEMONS=[5163444566]
    SUPPORT_CHAT="TogaSupport"
    OWNER_USERNAME="Redeye_ghoul"
    DONATION_LINK="lwdaalay"
    EVENT_LOGS="-1001745971242" 
    OWNER_ID="5122071509" 
    TIME_API_KEY=""
    ERROR_LOGS="-1001745971242" 
    BOT_NAME="AstorTestbot"
    STRICT_GBAN=True
    REDIS_URL="redis://OKI:Izaya123@+@redis-18548.c277.us-east-1-3.ec2.cloud.redislabs.com:18548/OKI-free-db"
    UPDATE_CHANNEL="TogaUpdates"
    MONGO_DB_URI="mongodb+srv://akari:akari123@cluster0.ewqoq9w.mongodb.net/?retryWrites=true&w=majority"
    BOT_USERNAME="AstorTestbot"
    REM_BG_API_KEY=""
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID="-1001679983263"
    STRICT_GMUTE=False
    SPAMWATCH_API=""
    OWNER_NAME="Abhinav"
    BANCODES=""
    REPOSITORY="GitHub.com/DARK-KING-2304/toga"
    ARQ_API_KEY=""
    ARQ_API_URL=""
    COTB=""
    

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
