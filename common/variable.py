from common.yaml_util import YamlUtil


def variable_code():
    # �� extract.yml �ж�ȡ admin_user_15881086121 ��ֵ
    code_value = YamlUtil().read_extract_yaml('admin_user_15881086121')
    # ��ȡ������������
    if code_value is None:
        # �����ȡ����ΪNone�������׳��쳣���߷���һ��Ĭ��ֵ
        raise ValueError("admin_user_15881086121 is None")
    data = YamlUtil().read_testcase_yaml('case_data.yml')
    # �� admin_user_15881086121 ��ֵ�滻����������������
    data['code_token'][0]['requests']['data']['code'] = code_value
    value = YamlUtil().func_yaml(data)
    print(f"Result: {value}")
    return [value]


def variable_token():
    # �� extract.yml �ж�ȡ token ��ֵ
    token_value = YamlUtil().read_extract_yaml('token')
    # ��ȡ������������
    test_data = YamlUtil().read_testcase_yaml('case_data.yml')
    # ����Ƿ�ɹ���ȡ�� token ֵ
    if token_value is None:
        raise ValueError("Token is None")
    # ���� nft ���ֵĲ�����������
    for case in test_data['nft']:
        # �������ͷ���Ƿ��� 'Authorization' �ֶ�
        if 'requests' in case and 'headers' in case['requests']:
            headers = case['requests']['headers']
            if 'Authorization' in headers:
                # �� token ֵ�滻�� 'Authorization' �ֶ���
                headers['Authorization'] = token_value
    # ʹ�� func_yaml ���������滻
    replaced_data = YamlUtil().func_yaml(test_data)

    return [replaced_data]


