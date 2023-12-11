from common import log_util
from common.yaml_util import YamlUtil


# case_data文件的${}变量替换成extract文件get_mobile_code_key的值
def variable_code(redis_data):
    key = redis_data[4]
    # 从 extract.yml 中读取 admin_user_key 的值
    code = YamlUtil().read_extract_yaml('get_mobile_code_key:1' + key)
    # 读取测试用例数据
    if code is None:
        # 如果提取数据为 None，可以抛出异常或者返回一个默认值
        error_message = "\033[1m\033[31m" + f"{'get_mobile_code_key:1' + key}未获取到验证码，请检查conftest.py手机号或case_data.yml账号密码是否正确" + "\033[0m"
        log_util.log_info(error_message)
        raise ValueError(error_message)
    # 读取 case_data.yml
    data = YamlUtil().read_testcase_yaml('test_case.yml')['code_token']
    value = YamlUtil().func_yaml(data, code)
    return value


# case_data文件的${}变量替换成extract文件Authorization的值
def variable_token():
    # 从 extract.yml 中读取 token 的值
    token_value = YamlUtil().read_extract_yaml('Authorization').encode('utf-8')
    # 读取测试用例数据
    test_data = YamlUtil().read_testcase_yaml('test_case.yml')
    # 检查是否成功读取到 token 值
    if token_value is None:
        raise ValueError("\033[1m\033[31m" + "Authorization为空" + "\033[0m")
    data = YamlUtil().read_testcase_yaml('test_case.yml')
    # 使用 func_yaml 方法处理替换
    replaced_data = YamlUtil().func_yaml(test_data, data)
    return [replaced_data]
