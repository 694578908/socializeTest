import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common import log_util
from common.ReadFile import read_ini
from common.color import colorize_text


def email_data():
    smtp_server = read_ini()['email']['smtp_server']
    smtp_username = read_ini()['email']['smtp_username']
    smtp_password = read_ini()['email']['smtp_password']
    smtp_port = read_ini()['email']['smtp_port']
    to_mail = read_ini()['email']['to_mail']
    from_email = read_ini()['email']['from_email']
    subject = read_ini()['email']['subject']
    send_enabled = read_ini()['email']['send_enabled'].lower()
    email_log = send_enabled != 'false'
    data = (smtp_server, smtp_username, smtp_password, smtp_port, to_mail, from_email, subject, email_log)
    return data


def send_email(data):
    smtp_server, smtp_username, smtp_password, smtp_port, to_mail, from_email, subject, email_log = data
    if not email_log:
        log_util.log_info('email是否开启:{}'.format(email_log))
        return
    if any(value is None or value == '' for value in data):
        return
    smtpserver = smtp_server
    smtpusername = smtp_username
    smtppassword = smtp_password
    smtpport = smtp_port

    tomail = to_mail
    fromemail = from_email
    # 邮箱标题
    subject_title = subject
    # 附件
    message = MIMEMultipart('related')
    message['From'] = fromemail
    message['To'] = tomail
    message['Subject'] = subject_title
    file_path = '/socializeTest/reports/report.html'
    abs_path = os.path.abspath(file_path)
    with open(abs_path, 'rb') as file:
        html_content = file.read()
        html_attachment = MIMEText(html_content, 'html', 'utf-8')
        message.attach(html_attachment)
    try:
        # 登录 smtp 服务器并发送邮件
        smtp = smtplib.SMTP_SSL(smtpserver, smtpport)
        log_util.log_info("SMTP 连接成功")
        smtp_login = smtp.login(smtpusername, smtppassword)
        if smtp_login[0] == 235:
            log_util.log_info("SMTP 登录成功")
        else:
            log_util.log_info(f"SMTP 登录失败，错误代码: {smtp_login[0]}, 错误消息: {smtp_login[1]}")
            return
        smtp_sendmail = smtp.sendmail(fromemail, tomail, message.as_string())
        if not smtp_sendmail:
            log_util.log_info("email发送成功")
        else:
            log_util.log_info(f"邮件发送失败，失败信息: {smtp_sendmail}")
        smtp.quit()

    except smtplib.SMTPException as e:
        email__error_message = colorize_text(f"Email发送失败. Exception: {e}")
        log_util.log_info(email__error_message)



