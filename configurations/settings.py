import os

BOT_TOKEN = '6925007502:AAEf-9tnhov2YztwFj7HyPWT4jyB8p_3XWE'
BOT_NAME = 'Tilo.Me-Massage-Bot'
PROJECT_DIR = os.getcwd()

while os.path.basename(PROJECT_DIR) != BOT_NAME:
    PROJECT_DIR = os.path.dirname(PROJECT_DIR)
