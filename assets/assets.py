import assets.languages as languages

def set_language(language):
    for var_name in languages.languages_data[language]:
        globals()[var_name] = languages.languages_data[language][var_name]
