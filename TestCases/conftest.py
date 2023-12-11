import pytest
import logging
from common.ReadFile import read_ini
from common.log_util import clear_logs, disable_log
from common.yaml_util import YamlUtil

# redis����������
@pytest.fixture(scope='session')
def redis_data():
    host = read_ini()['redis']['host']
    password = read_ini()['redis']['password']
    port = read_ini()['redis']['port']
    db = read_ini()['redis']['db']
    key = read_ini()['redis']['key']  # ��Ҫ�Զ����޸���Ҫ��ȡ�ֻ���֤��
    data = (host, password, port, db, key)
    return data


# log��־����������
@pytest.fixture(scope='session', autouse=True)
def log_data():
    dirname = read_ini()['log']['dirname']  # �ļ�������
    log_name = read_ini()['log']['log_name']  # �ļ�����Ĭ��Ϊ��
    log_name_format = read_ini()['log']['log_name_format']  # Ĭ���ļ�������-��-�ո�ʽ��ʾ
    log_level = getattr(logging, read_ini()['log']['log_level'], logging.DEBUG)  # ��־�ȼ�
    log_format = read_ini()['log']['log_format']  # ��־��ʽ
    disable_logging_str = read_ini()['log']['disable_logging'].lower()
    disable_logging = disable_logging_str != 'false'  # True������־��False�ر���־

    data = (dirname, log_name, log_name_format, log_level, log_format)
    disable_log(disable_logging, data)
    return data


# ʵʱ���extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_extract_yaml():
    YamlUtil().clear_extract_yaml()
    yield


# ��ʱ���log��־
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # ���ù���ʱ�䣨��СʱΪ��λ��
    expiration_hours = int(read_ini()['log']['expiration_hours'])
    clear_logs(expiration_hours)
    yield
