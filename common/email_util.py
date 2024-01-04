import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from common import log_util
from common.ReadFile import read_ini


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
        log_util.log_info(email_log)
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

    # 登录 smtp 服务器并发送邮件
    smtp = smtplib.SMTP_SSL(smtpserver, smtpport)
    smtp.login(smtpusername, smtppassword)
    smtp.sendmail(fromemail, tomail, message.as_string())
    smtp.quit()
