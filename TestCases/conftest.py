import pytest
from common import log_util
from common.yaml_util import YamlUtil


# ���extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
    yield


# ��ʱ���log��־
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # ���ù���ʱ�䣨��СʱΪ��λ��
    expiration_hours = 48
    log_util.clear_logs(expiration_hours)
    yield


# @pytest.fixture(scope='session', autouse=True)
# def setup_logging():
#     # �ڲ��ԻỰ���������Թ��̣���ʼǰ��ʼ����־
#     log_util.init_logging()


# redis��������
@pytest.fixture(scope='session')
def redis_data():
    host = '172.16.1.5'
    password = 'Lzd%2c6c1181ebC6cc'
    port = 6379
    db = 7
    key = '15881086121'  # ��Ҫ�Զ����ȡredis�ֻ���֤��
    data = (host, password, port, db, key)
    return data
