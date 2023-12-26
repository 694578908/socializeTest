import redis
from common.yaml_util import YamlUtil
from common import log_util


# 获取redis的value并写入yaml
def read_redis(redis_data):
    host, password, port, db, key = redis_data
    redis_client = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)

    folder_key = 'get_mobile_code_key:1'
    full_key = folder_key + key
    value = redis_client.get(full_key)

    if value is None:
        error_message = "\033[1m\033[31m" + f"{full_key}未获取到验证码，请检查config.ini,test_case.yml手机号是否正确(手机号切勿设置白名单)" + "\033[0m"
        log_util.log_info(error_message)
        raise ValueError(error_message)

    # 将键值对构建为字典
    data = {'code': value}
    YamlUtil().write_extract_yaml(data)
