import redis
from common.yaml_util import YamlUtil


# 获取redis的value并写入yaml
def read_redis(redis_data):
    host, password, port, db, key = redis_data
    redis_client = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)
    # 提取键对应的值
    number = ('admin_user_' + key)
    value = redis_client.get(number)
    # 将键值对构建为字典
    data = {number: value}
    YamlUtil().write_extract_yaml(data)
