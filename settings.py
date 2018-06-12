from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

DATA_FOLDER=getenv('DATA_FOLDER')

DB_NAME = "coubs.db"
DB_LOCATION = DATA_FOLDER + DB_NAME

SLACK_WEBHOOK = getenv('SLACK_WEBHOOK')