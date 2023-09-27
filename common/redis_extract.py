import redis
from common.yaml_util import YamlUtil


def read_redis():
    # 定义连接参数
    host = '172.16.1.5'
    port = 6379
    password = 'Lzd%2c6c1181ebC6cc'
    db = '7'

    # 连接到Redis数据库
    redis_client = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)
    # 要提取的键
    key = 'admin_user_15881086121'

    # 提取键对应的值
    value = redis_client.get(key)
    # 将键值对构建为字典
    data = {key: value}
    YamlUtil().write_extract_yaml(data)

