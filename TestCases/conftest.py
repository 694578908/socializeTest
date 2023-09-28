import pytest
import logging
from common.log_util import clear_logs, init_logging
from common.yaml_util import YamlUtil


# redis参数配置项
@pytest.fixture(scope='session')
def redis_data():
    host = '172.16.1.5'
    password = 'Lzd%2c6c1181ebC6cc'
    port = 6379
    db = 7
    key = '158810861211'  # 需要自定义修改想要获取手机验证码
    data = (host, password, port, db, key)
    return data

# log日志参数配置项
@pytest.fixture(scope='session', autouse=True)
def log_data():
    dirname = 'log'  # 文件夹名称
    log_name = '{}.log'  # 文件名，默认为空
    log_name_format = "%Y-%m-%d"  # 文件名以时间格式显示
    log_level = logging.DEBUG  # 日志等级
    log_format = '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'  # 日志格式
    data = (dirname, log_name, log_name_format, log_level, log_format)
    init_logging(data)  # 确保日志记录器和处理器已经初始化
    return data


# 清除extract.yml
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
