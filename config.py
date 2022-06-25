import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5584381358:AAF7EKL0lZcqhY4m315YC-Mt1ubnyxmmKUg")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","f495ff93-da4a-4e58-b4ca-bad8256dee35")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME","")
