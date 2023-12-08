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
            result = {}  # 创建一个新的字典来存储处理后的数据
            for key, value in data.items():
                # 递归处理嵌套的字典
                result[key] = self.func_yaml(value, code)
            return result
        elif isinstance(data, list):
            # 处理列表中的每个项
            return [self.func_yaml(item, code) for item in data]
        elif isinstance(data, str):
            # 使用正则表达式匹配字符串中的 ${variable} 模式
            matches = re.findall(r'\${(\w+)}', data)
            for match in matches:
                print(f"匹配到变量：{match}，代码中的值：{code}")
                data = data.replace(f'${{{match}}}', str(code))
            return data  # 返回处理后的字符串

        print(f"处理后的数据：{data}")
        return data



