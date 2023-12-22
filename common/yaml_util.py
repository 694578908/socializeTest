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
                data = value[key_name]
                print(data)
                return value[key_name]
            return value

    def extra_read_yaml(self, yaml_name, key_name):
        data = self.read_testcase_yaml(yaml_name, key_name)
        req_info = data["req_info"]

    def func_yaml(self, data, code):
        if isinstance(data, dict):
            result = {}
            for key, value in data.items():
                # 处理不同类型的键
                if key.startswith('get_mobile_code_key:'):
                    # 提取键号并将其附加到新键
                    new_key = f'get_mobile_code_key:{code}'
                    result[new_key] = self.func_yaml(value, code)
                elif key == 'Authorization':
                    # 处理 'token' 键
                    result[key] = self.func_yaml(value, code)
                else:
                    result[key] = self.func_yaml(value, code)
            return result
        elif isinstance(data, list):
            return [self.func_yaml(item, code) for item in data]
        elif isinstance(data, str):
            matches = re.findall(r'\${(\w+)}', data)
            for match in matches:
                data = data.replace(f'${{{match}}}', str(code))
            return data
        return data



    # def func_yaml(data, variables):
    #     if isinstance(data, dict):
    #         result = {}
    #         for key, value in data.items():
    #             result[key] = replace_variables(value, variables)
    #         return result
    #     elif isinstance(data, list):
    #         return [replace_variables(item, variables) for item in data]
    #     elif isinstance(data, str):
    #         for variable, replacement in variables.items():
    #             data = data.replace(f"${{{variable}}}", str(replacement))
    #         return data
    #     return data


