#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24972860"))
API_HASH = environ.get("API_HASH", "94b5189df033bd8b71352b3bed0b44fc")
BOT_TOKEN = environ.get("BOT_TOKEN", "8187113163:AAGjWbYoI-Eq3blW33eV01DdnmezEDOK1wI")

OWNER = int(environ.get("OWNER", "684325515"))
CREDIT = environ.get("CREDIT", "𝘼𝙯𝙖𝙯𝙚𝙡")

TOTAL_USER = os.environ.get('TOTAL_USERS', '684325515').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '684325515').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
