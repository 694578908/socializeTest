import configparser
import os


def read_ini(file_path='/socializeTest/config.ini'):
    abs_path = os.path.abspath(file_path)
    print(f"Absolute path: {abs_path}")

    config = configparser.ConfigParser()
    config.read(abs_path, encoding='utf-8-sig')
    return config


