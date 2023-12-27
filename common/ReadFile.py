import configparser
import os


def read_ini(file_path='/socializeTest1/config.ini'):
    abs_path = os.path.abspath(file_path)
    config = configparser.ConfigParser()
    config.read(abs_path, encoding='utf-8-sig')
    return config


