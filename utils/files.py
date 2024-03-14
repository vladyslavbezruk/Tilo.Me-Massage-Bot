import codecs
import json


def load_file(file_path):
    with codecs.open(file_path, encoding='utf-8') as file:
        return json.loads(file.read())


def save_file(data, file_path):
    with codecs.open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file)
