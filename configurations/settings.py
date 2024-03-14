import os

BOT_TOKEN = '6925007502:AAHGEGOuUgTNiS995sXZA0gde3mPa4bsAbw'
BOT_NAME = 'Tilo.Me-Massage-Bot'
PROJECT_DIR = os.getcwd()

while os.path.basename(PROJECT_DIR) != BOT_NAME:
    PROJECT_DIR = os.path.dirname(PROJECT_DIR)
