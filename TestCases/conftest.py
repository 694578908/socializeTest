import pytest
from common import log_util
from common.yaml_util import YamlUtil


# 清除extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
    yield


# 定时清除log日志
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # 设置过期时间（以小时为单位）
    expiration_hours = 48
    log_util.clear_logs(expiration_hours)
    yield


# @pytest.fixture(scope='session', autouse=True)
# def setup_logging():
#     # 在测试会话（整个测试过程）开始前初始化日志
#     log_util.init_logging()


# redis参数配置
@pytest.fixture(scope='session')
def redis_data():
    host = '172.16.1.5'
    password = 'Lzd%2c6c1181ebC6cc'
    port = 6379
    db = 7
    key = '15881086121'  # 需要自定义获取redis手机验证码
    data = (host, password, port, db, key)
    return data
