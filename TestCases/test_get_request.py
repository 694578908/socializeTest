import pytest
import allure
from common.get_request import case_request_response
from common.redis_extract import read_redis
from common.yaml_util import YamlUtil


@allure.epic('社交用户端')
class TestRequest:

    # 登录账号密码
    @allure.feature('登录功能模块')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('test_case.yml', 'login'))
    def test_case_login(self, case, redis_data):
        case_request_response(case)
        read_redis(redis_data)  # 调取redis并把验证码写入extract.yml文件里

    # 提交验证码
    @allure.feature('登录功能模块')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('test_case.yml', 'code_token'))
    def test_case_gettoken(self, case):
        case_request_response(case)

    @allure.feature('接口功能模块')
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('test_case.yml', 'nft'))
    def test_case_nft(self, case):
        case_request_response(case)
