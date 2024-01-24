import time

import allure
import requests
import json

from common import log_util


class RequestUtil:
    session = requests.session()

    # 发送请求
    def send_requests(self, title, method, url, headers, data, **kwargs):
        method = str(method).lower()
        rep = None
        timeout_value = 5
        start_time = time.time()
        if method == 'get':
            rep = RequestUtil.session.request(method=method, url=url, params=data, headers=headers,
                                              timeout=timeout_value,
                                              **kwargs)
        else:
            data = json.dumps(data)
            rep = RequestUtil.session.request(method=method, data=data, url=url, headers=headers, timeout=timeout_value,
                                              **kwargs)

        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_rounded = round(elapsed_time, 2)

        response_timeout = {'接口限制最大请求时间': timeout_value, '接口实际请求时间': elapsed_time_rounded}
        response_url = {'method': rep.request.method, 'url': rep.url}
        allure.attach(json.dumps(response_timeout, ensure_ascii=False, indent=2), name="接口响应时间",
                      attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(response_url, ensure_ascii=False, indent=2), name="请求地址",
                      attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(headers, ensure_ascii=False, indent=2), name="请求头",
                      attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(rep.json(), ensure_ascii=False, indent=2), name="接口响应",
                      attachment_type=allure.attachment_type.JSON)
        try:
            assert rep.status_code == 200
            log_status = '接口请求成功'
        except AssertionError:
            log_status = '接口请求失败'

        log_util.log_info(
            '{}>>>>接口状态码:{},接口限制最大请求时间:{}秒,实际请求时间:{}秒'.format(log_status, rep.status_code, timeout_value,
                                                              elapsed_time_rounded))
        log_util.log_info('用例标题:{}'.format(title))
        log_util.log_info('请求地址:{},请求头:{}'.format(rep.url, rep.headers))
        log_util.log_info('请求参数:{}'.format(rep.request.body))
        log_util.log_info('接口返回信息为:{}'.format(rep.json()))

        if not log_status == '接口请求成功':
            raise AssertionError(log_status)
        return rep.text
