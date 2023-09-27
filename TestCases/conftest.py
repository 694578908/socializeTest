import pytest
from common import log_util
from common.yaml_util import YamlUtil

# 清除extract.yml
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
    yield

# 清除log日志
@pytest.fixture(scope="session", autouse=True)
def clear_log():
    # 设置过期时间（以小时为单位）
    expiration_hours = 1
    log_util.clear_logs(expiration_hours)
    yield


