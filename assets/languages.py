import utils.jsons as jsons
from configurations.settings import *

available_languages = ['ua', 'en']

languages_data = {}


def load_languages():
    for language in available_languages:
        file_path = os.path.join(PROJECT_DIR, 'assets', 'lang', language + '.json')
        languages_data[language] = jsons.load_json(file_path)
