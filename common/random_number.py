import random
from common.yaml_util import YamlUtil


def random_phone_number(key):
    phone_header_list = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139']
    phone_header = random.choice(phone_header_list)
    phone_data_list = '0123456879'
    phone_data = ''.join(random.sample(phone_data_list, k=8))
    phone_number = phone_header + phone_data
    YamlUtil().write_extract_yaml({key: phone_number})

