import configparser


def read_ini(file_path='/socializeTest/config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path, encoding='utf-8-sig')
    return config


