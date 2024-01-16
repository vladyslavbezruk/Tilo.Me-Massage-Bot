import utils.files as files


def load_json(path):
    return files.load_file(path)


def save_json(data, path):
    files.save_file(data, path)