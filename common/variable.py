from common import log_util
from common.yaml_util import YamlUtil


# def read_and_replace_variable(key, error_message):
#     # 从 extract.yml 中读取值
#     value = YamlUtil().read_extract_yaml(key)
#     # 如果提取数据为 None，抛出异常
#     if value is None:
#         log_util.log_info(error_message)
#         raise ValueError(error_message)
#     # 读取 test_case.yml
#     data = YamlUtil().read_testcase_yaml('test_case.yml')
#     # 使用 func_yaml 方法处理替换
#     replaced_data = YamlUtil().func_yaml(data, value)
#     return [replaced_data]
#
#
# # test_case文件的${}变量替换成extract文件get_mobile_code_key的值
# def variable_code(redis_data):
#     key = redis_data[4]
#     error_message = f"\033[1m\033[31m{'get_mobile_code_key:1' + key}未获取到验证码，请检查config.ini,test_case.yml手机号是否正确(手机号切勿设置白名单)\033[0m"
#     return read_and_replace_variable('get_mobile_code_key:1' + key, error_message)
#
#
# # test_case文件的${}变量替换成extract文件Authorization的值
# def variable_token():
#     error_message = "\033[1m\033[31mAuthorization为空\033[0m"
#     return read_and_replace_variable('Authorization', error_message)


def read_and_replace_variables(keys_and_messages):
    value = {}
    for key, error_message in keys_and_messages.items():
        value = YamlUtil().read_extract_yaml(key)
        if value is None:
            log_util.log_info(error_message)
            raise ValueError(error_message)
        # now_value[key] = value
        print(value)
    data = YamlUtil().read_testcase_yaml('test_case.yml')
    replaced_data = YamlUtil().func_yaml(data, value)
    return [replaced_data]


def variable_code(redis_data):
    keys_and_messages = {
        f'get_mobile_code_key:1{redis_data[4]}': f"\033[1m\033[31m{'get_mobile_code_key:1{redis_data[4]}'}未获取到验证码，请检查config.ini,test_case.yml手机号是否正确(手机号切勿设置白名单)\033[0m",
        # 添加其他 key 和对应的错误消息
    }

    return read_and_replace_variables(keys_and_messages)


def variable_token():
    keys_and_messages = {
        'Authorization': "\033[1m\033[31mAuthorization为空\033[0m",
        # 添加其他 key 和对应的错误消息
    }
    return read_and_replace_variables(keys_and_messages)
