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
    BAN_STICKER="kans"
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="YourPervertSenpai"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"
    
    #change
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
    OWNER_USERNAME="izuya"
    DONATION_LINK="https://www.paypal.me/PaulSonOfLars"
    EVENT_LOGS="-1001548936254" 
    OWNER_ID="5163444566" 
    TIME_API_KEY="" #gift from meow
    ERROR_LOGS="-1001417928763" 
    BOT_NAME="toga_robot"
    STRICT_GBAN=True
    REDIS_URL=""
    ARQ_API_KEY="CZGPYC-SCMRAI-EKQNGY-ZRFYGZ-ARQ"
    UPDATE_CHANNEL="AnicadeUpdates"
    MONGO_DB_URI=""
    BOT_USERNAME="Toga_Robot"
    REM_BG_API_KEY="K2Rc"
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID="-1001417928763"
    STRICT_GMUTE=False
    NETWORK_USERNAME="Anicademia"
    NETWORK_NAME="Anicade"
    AFKVID=""
    GROUP_ALIVE_PIC=""
    SUMI_STATS_PIC=""
    SUMI_WELCOME=""
    SUMI_OWNER_WEL_IMG=""
    SUMI_DISPACHER_PIC=""
    SUMI_HELP_PIC=""
    PM_IMAGE=""
    GROUPSTART_VID=""
    SUMI_DIS_WEL=""
    SPAMWATCH_API="9x__eKEBWQFj~t~zgUWkSk8BWSsWYaAcDWFEITQX1eKNd3CswakpUVYGt5hcH06n"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    OWNER_NAME = "izuya"
    COTB = "izuya"
    BANCODES = ""
    REPOSITORY = "GitHub.com/kac-chan/togap"
    RED7_TOKEN = ""

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
