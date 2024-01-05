import time
import pytest
import os

from common.email_util import send_email, email_data
from common.html_util import HTMLModifier, HTMLReportCleaner

if __name__ == '__main__':
    HTMLReportCleaner().clean_old_report()
    pytest.main()
    os.system("allure generate ./reports/allure-temp -o ./reports/allure-report --clean")

    # 调用修改html方法
    HTMLModifier().edit_html()
    # 获取邮件信息
    email_info = email_data()
    # 发送电子邮件
    send_email(email_info)
