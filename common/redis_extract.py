import redis
from common.yaml_util import YamlUtil
from common import log_util
from common.color import colorize_text


# 获取redis的value并写入yaml
def read_redis(redis_data):
    host, password, port, db, key = redis_data
    try:
        redis_client = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)
        response = redis_client.ping()
        log_util.log_info('Redis是否连接成功:{}'.format(response))
        if response:
            folder_key = 'get_mobile_code_key:1'
            full_key = folder_key + key
            value = redis_client.get(full_key)

            if value is None:
                error_message = colorize_text(f"{full_key}未获取到验证码，请检查config.ini,test_case.yml手机号是否正确(手机号切勿设置白名单)")
                log_util.log_info(error_message)
                raise ValueError(error_message)

            # 将键值对构建为字典
            data = {'code': value}
            YamlUtil().write_extract_yaml(data)

        else:
            print_response = colorize_text("Redis连接失败,请检查config.ini账号密码是否输入正确")
            log_util.log_info(print_response)
            raise ValueError(print_response)
    except redis.exceptions.ConnectionError:
        # 处理连接超时的逻辑
        timeout_error_message = colorize_text("Redis连接超时，请检查连接配置和网络是否正常")
        log_util.log_info(timeout_error_message)
        raise ValueError(timeout_error_message)
    redis_client.close()


def redis_extract_number(redis_data):
    host, password, port, db, key = redis_data
    try:
        redis_client = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)
        response = redis_client.ping()
        log_util.log_info('Redis是否连接成功:{}'.format(response))
        if response:
            folder_key = 'get_mobile_code_key:1'
            mobile_value = YamlUtil().read_extract_yaml('mobile')
            full_key = folder_key + mobile_value
            value = redis_client.get(full_key)

            if value is None:
                error_message = colorize_text(f"{full_key}未获取到验证码，请检查config.ini,test_case.yml手机号是否正确(手机号切勿设置白名单)")
                log_util.log_info(error_message)
                raise ValueError(error_message)

            # 将键值对构建为字典
            data = {'code1': value}
            YamlUtil().write_extract_yaml(data)

        else:
            print_response = colorize_text("Redis连接失败,请检查config.ini账号密码是否输入正确")
            log_util.log_info(print_response)
            raise ValueError(print_response)
    except redis.exceptions.ConnectionError:
        # 处理连接超时的逻辑
        timeout_error_message = colorize_text("Redis连接超时，请检查连接配置和网络是否正常")
        log_util.log_info(timeout_error_message)
        raise ValueError(timeout_error_message)
    redis_client.close()
