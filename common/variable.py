from common.yaml_util import YamlUtil


def variable_code():
    # 从 extract.yml 中读取 admin_user_15881086121 的值
    code_value = YamlUtil().read_extract_yaml('admin_user_15881086121')
    # 读取测试用例数据
    if code_value is None:
        # 如果提取数据为None，可以抛出异常或者返回一个默认值
        raise ValueError("admin_user_15881086121 is None")
    data = YamlUtil().read_testcase_yaml('case_data.yml')
    # 将 admin_user_15881086121 的值替换到测试用例数据中
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
        raise ValueError("Token is None")
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


