import time
import pytest
import os

from common.email_util import send_email, email_data

if __name__ == '__main__':

    html_report_path = './reports/report.html'

    # 清理旧的 HTML 报告文件（如果存在）
    if os.path.exists(html_report_path):
        os.remove(html_report_path)

    # 运行 pytest 并生成 HTML 报告
    pytest.main(['--html=' + html_report_path, '--self-contained-html'])
    os.system("allure generate ./reports/allure-temp -o ./reports/allure-report --clean")

    # 获取邮件信息
    email_info = email_data()
    # 发送电子邮件
    send_email(email_info)
