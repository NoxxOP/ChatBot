import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("20071630")) 
API_HASH = os.getenv("11d0d49035cfa33964c687e4480fef0d")

# Bot Token / String Session
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING1 = os.getenv("STRING_SESSION", None)

# Database
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://pusers:nycreation@nycreation.pd4klp1.mongodb.net/?retryWrites=true&w=majority&appName=NYCREATION")

# Owner / Admin
OWNER_ID = int(os.getenv("8306720320"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME")

# Support / Updates
SUPPORT_GRP = os.getenv("SUPPORT_GRP", "https://t.me/JAWANON_KI_TOLI")
UPDATE_CHNL = os.getenv("UPDATE_CHNL", "https://t.me/JAWANON_KA_ADDA")
