import json

import allure
import jsonpath

from common import log_util
from common.color import colorize_text
from common.count import count
from common.request_util import RequestUtil
from common.variable import read_and_replace_variables, extract_response_data


def case_request_response(case):
    count(case)  # 打印用例执行次数
    if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
        if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
            allure.dynamic.title(case['name'])
            replaced_case = read_and_replace_variables(case)
            title = case['name']
            headers = case['requests']['headers']
            url = case['requests']['url']
            data = case['requests']['data']
            method = case['requests']['method']
            result = RequestUtil().send_requests(title, method, url, headers, data)
            res = json.loads(result)
            if 'extract' in replaced_case:
                extraction_dict = replaced_case['extract']
                # 使用extract的表达式提取接口响应参数并写入extract.yml
                extract_response_data(extraction_dict, result)

            allure.attach(json.dumps(data, ensure_ascii=False, indent=2), name="请求参数",
                          attachment_type=allure.attachment_type.JSON)
            try:
                assert res['code'] == case['validate'][0]['equals']['code']
                log_status = '状态Code断言成功'
            except AssertionError:
                log_status = '状态Code断言失败'

            allure.attach(f"实际结果:{res['code']}，预期结果{case['validate'][0]['equals']['code']}", name=log_status)
            log_util.log_info(
                '{}>>>>接口返回预期结果code应为: {}，实际为:{}'.format(log_status, case['validate'][0]['equals']['code'], res['code']))
            if not log_status == '状态Code断言成功':
                raise AssertionError(log_status)

        else:
            error_message = colorize_text("在yml文件requests目录下必须要有method,url,data,headers")
            log_util.log_info(error_message)
            raise ValueError(error_message)
    else:
        error_message = colorize_text("yml一级关键字必须包含:name,requests,validate")
        log_util.log_info(error_message)
        raise ValueError(error_message)
    return url
