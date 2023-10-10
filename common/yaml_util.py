import os
import yaml


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
                data=value[key_name]
                print(data)
                return value[key_name]

            return value


    def extra_read_yaml(self,yaml_name, key_name):

        data=self.read_testcase_yaml(yaml_name, key_name)
        req_info=data["req_info"]




    def func_yaml(self, data, variable_whitelist=None):
        if variable_whitelist is None:
            variable_whitelist = set()  # 默认情况下，白名单为空
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str) and '${' in value and '}' in value:
                    start = value.index('${')
                    end = value.index('}')
                    func_name = value[start + 2:end]

                    if func_name in variable_whitelist:
                        # 仅当变量名在白名单中时执行替换操作
                        data[key] = value[0:start] + str(eval(func_name)) + value[end + 1:]
                elif isinstance(value, dict):
                    # 递归处理嵌套的字典
                    data[key] = self.func_yaml(value, variable_whitelist)
        return data
