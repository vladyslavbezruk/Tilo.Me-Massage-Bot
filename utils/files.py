import codecs
import json


def load_file(FilePath):
    with codecs.open(FilePath, encoding='utf-8') as file:
        return json.loads(file.read())


def save_file(data, FilePath):
    with codecs.open(FilePath, "w", encoding='utf-8') as file:
        json.dump(data, file)
