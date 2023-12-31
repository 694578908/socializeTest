import json
import jsonpath
import allure
from common import log_util
from common.request_util import RequestUtil
from common.variable import read_and_replace_variables, extract_response_data
from common.count import count
from common.color import colorize_text


def case_request_response(case):
    count(case)  # 打印用例执行次数
    if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
        if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
            allure.dynamic.title(case['name'])
            replaced_case = read_and_replace_variables(case)
            headers = case['requests']['headers']
            url = case['requests']['url']
            data = case['requests']['data']
            method = case['requests']['method']
            result = RequestUtil().send_requests(method, url, headers, data)
            res = (json.loads(result))
            if 'extract' in replaced_case:
                extraction_dict = replaced_case['extract']
                # 使用extract的表达式提取接口响应参数并写入extract.yml
                extract_response_data(extraction_dict, result)
            log_util.log_info('用例标题:{},请求地址:{},请求头:{},请求参数:{}'.format(case['name'], url, headers, data))
            log_util.log_info('实际结果接口返回信息为:{}'.format(result))
            log_util.log_info('预期结果：code 应为: {}'.format(case['validate'][0]['equals']['code']))

            request_info = {"method": method, "url": url}
            allure.attach(json.dumps(request_info, ensure_ascii=False, indent=2), name="请求地址",
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(json.dumps(headers, ensure_ascii=False, indent=2), name="请求头",
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(json.dumps(data, ensure_ascii=False, indent=2), name="请求参数",
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(json.dumps(result, ensure_ascii=False, indent=2), name="接口响应",
                          attachment_type=allure.attachment_type.JSON)
            try:
                assert res['code'] == case['validate'][0]['equals']['code']
                allure.attach(f"实际结果:{res['code']}，预期结果{case['validate'][0]['equals']['code']}", name="状态Code断言成功")
            except AssertionError:
                allure.attach(f"实际结果:{res['code']}，预期结果{case['validate'][0]['equals']['code']}", name="状态Code断言失败")
                raise
        else:
            error_message = colorize_text("在yml文件requests目录下必须要有method,url,data,headers")
            log_util.log_info(error_message)
            raise ValueError(error_message)
    else:
        error_message = colorize_text("yml一级关键字必须包含:name,requests,validate")
        log_util.log_info(error_message)
        raise ValueError(error_message)
