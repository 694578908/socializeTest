import pytest
import logging
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


from common.ReadFile import read_file
from common.log_util import clear_logs, disable_log
from common.yaml_util import YamlUtil


# redis参数配置项
@pytest.fixture(scope='session')
def redis_data():
    host = read_file.read_ini()['redis']['host']
    password = read_file.read_ini()['redis']['password']
    port = read_file.read_ini()['redis']['port']
    db = read_file.read_ini()['redis']['db']
    key = read_file.read_ini()['redis']['key']  # 需要自定义修改想要获取手机验证码
    data = (host, password, port, db, key)
    return data


# log日志参数配置项
@pytest.fixture(scope='session', autouse=True)
def log_data():
    dirname = 'log'  # 文件夹名称
    log_name = '{}.log'  # 文件名，默认为空
    log_name_format = "%Y-%m-%d"  # 默认文件名以年-月-日格式显示
    log_level = logging.DEBUG  # 日志等级
    log_format = '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'  # 日志格式
    disable_logging = True  # True开启日志，False关闭日志

    data = (dirname, log_name, log_name_format, log_level, log_format)
    disable_log(disable_logging, data)
    return data


# 实时清除extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_extract_yaml():
    YamlUtil().clear_extract_yaml()
    yield


# 定时清除log日志
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # 设置过期时间（以小时为单位）
    expiration_hours = 48
    clear_logs(expiration_hours)
    yield



# 定时清除log日志
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # 设置过期时间（以小时为单位）
    expiration_hours = 48
    clear_logs(expiration_hours)
    yield