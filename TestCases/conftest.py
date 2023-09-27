import pytest
from common import log_util
from common.yaml_util import YamlUtil

# ���extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
    yield

# ���log��־
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # ���ù���ʱ�䣨��СʱΪ��λ��
    expiration_hours = 1
    log_util.clear_logs(expiration_hours)
    yield


