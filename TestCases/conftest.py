import pytest
import logging
from common.log_util import clear_logs, init_logging
from common.yaml_util import YamlUtil


# redis����������
@pytest.fixture(scope='session')
def redis_data():
    host = '172.16.1.5'
    password = 'Lzd%2c6c1181ebC6cc'
    port = 6379
    db = 7
    key = '158810861211'  # ��Ҫ�Զ����޸���Ҫ��ȡ�ֻ���֤��
    data = (host, password, port, db, key)
    return data

# log��־����������
@pytest.fixture(scope='session', autouse=True)
def log_data():
    dirname = 'log'  # �ļ�������
    log_name = '{}.log'  # �ļ�����Ĭ��Ϊ��
    log_name_format = "%Y-%m-%d"  # �ļ�����ʱ���ʽ��ʾ
    log_level = logging.DEBUG  # ��־�ȼ�
    log_format = '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'  # ��־��ʽ
    data = (dirname, log_name, log_name_format, log_level, log_format)
    init_logging(data)  # ȷ����־��¼���ʹ������Ѿ���ʼ��
    return data


# ���extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_extract_yaml():
    YamlUtil().clear_extract_yaml()
    yield


# ��ʱ���log��־
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # ���ù���ʱ�䣨��СʱΪ��λ��
    expiration_hours = 48
    clear_logs(expiration_hours)
    yield
