from common import log_util
from common.yaml_util import YamlUtil


# extract的token替换case_data文件的${}变量
def variable_code(redis_data):
    key = redis_data[4]
    # 从 extract.yml 中读取 admin_user_key 的值
    code_value = YamlUtil().read_extract_yaml('admin_user_' + key)
    # 读取测试用例数据
    if code_value is None:
        # 如果提取数据为None，可以抛出异常或者返回一个默认值
        error_message = "\033[1m\033[31m" + f"{'admin_user_' + key}未获取到验证码，请检查conftest.py手机号是否正确" + "\033[0m"
        log_util.log_info(error_message)
        raise ValueError(error_message)
    # 从 case_data.yml 中读取
    data = YamlUtil().read_testcase_yaml('case_data.yml')
    # 将case_data.yml的code 的值替换到测试用例数据中
    data['code_token'][0]['requests']['data']['code'] = code_value
    value = YamlUtil().func_yaml(data)
    print(f"Result: {value}")
    return [value]


def variable_token():
    # 从 extract.yml 中读取 token 的值
    token_value = YamlUtil().read_extract_yaml('token')
    # 读取测试用例数据
    test_data = YamlUtil().read_testcase_yaml('case_data.yml')
    # 检查是否成功读取到 token 值
    if token_value is None:
        raise ValueError("\033[1m\033[31m" + "token为空" + "\033[0m")
    # 遍历 nft 部分的测试用例数据
    for case in test_data['nft']:
        # 检查请求头中是否有 'Authorization' 字段
        if 'requests' in case and 'headers' in case['requests']:
            headers = case['requests']['headers']
            if 'Authorization' in headers:
                # 将 token 值替换到 'Authorization' 字段中
                headers['Authorization'] = token_value
    # 使用 func_yaml 方法处理替换
    replaced_data = YamlUtil().func_yaml(test_data)

    return [replaced_data]
