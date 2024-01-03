import os
import yaml
import re


class YamlUtil:

    # 读取extract.yml
    def read_extract_yaml(self, key):
        try:
            with open(os.getcwd() + "/data/extract.yml", mode='r', encoding='utf-8')as f:
                value = yaml.load(stream=f, Loader=yaml.FullLoader)
                return value[key]
        except Exception as e:
            print(f"{e}")
            return None

    # 写入extract.yml
    def write_extract_yaml(self, data):
        with open(os.getcwd() + "/data/extract.yml", mode='a', encoding='utf-8')as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除extract.yml
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/data/extract.yml", mode='w', encoding='utf-8')as f:
            f.truncate()

    # 读取yml文件
    def read_testcase_yaml(self, yaml_name, key_name=None):
        with open(os.getcwd() + "/data/" + yaml_name, mode='r', encoding='utf-8')as f:
            value = yaml.safe_load(stream=f)
            if key_name:
                return value[key_name]
            return value

    def extra_read_yaml(self, yaml_name, key_name):
        data = self.read_testcase_yaml(yaml_name, key_name)
        req_info = data["req_info"]

    # def func_yaml(self, data, code):
    #     if isinstance(data, dict):
    #         result = {}
    #         for key, value in data.items():
    #             # 处理不同类型的键
    #             if key.startswith('get_mobile_code_key:'):
    #                 # 提取键号并将其附加到新键
    #                 new_key = f'get_mobile_code_key:{code}'
    #                 result[new_key] = self.func_yaml(value, code)
    #             elif key == 'Authorization':
    #                 # 处理 'token' 键
    #                 result[key] = self.func_yaml(value, code)
    #             else:
    #                 result[key] = self.func_yaml(value, code)
    #         return result
    #     elif isinstance(data, list):
    #         return [self.func_yaml(item, code) for item in data]
    #     elif isinstance(data, str):
    #         matches = re.findall(r'\${(\w+)}', data)
    #         for match in matches:
    #             data = data.replace(f'${{{match}}}', str(code))
    #         return data
    #     return data

    def func_yaml(self, test_cases, placeholder_values):
        if placeholder_values is None:
            return test_cases
        for test_case_key, test_case in test_cases.items():
            request = test_case

            # 处理 url
            if 'url' in request and isinstance(request['url'], str):
                for placeholder, new_value in placeholder_values.items():
                    if f"${{{placeholder}}}" in request['url']:
                        request['url'] = request['url'].replace(f"${{{placeholder}}}", str(new_value))

                # 处理 headers
                if 'headers' in request and isinstance(request['headers'], dict):
                    for key, value in request['headers'].items():
                        if isinstance(value, str):
                            for placeholder, new_value in placeholder_values.items():
                                if f"${{{placeholder}}}" in value:
                                    request['headers'][key] = value.replace(f"${{{placeholder}}}", str(new_value))

                # 处理 data
                if 'data' in request and isinstance(request['data'], dict):
                    for key, value in request['data'].items():
                        if isinstance(value, str):
                            for placeholder, new_value in placeholder_values.items():
                                if f"${{{placeholder}}}" in value:
                                    request['data'][key] = value.replace(f"${{{placeholder}}}", str(new_value))

        return test_cases
