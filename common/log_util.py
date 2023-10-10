import logging
import os
from datetime import datetime, timedelta
import time

# 创建一个全局的日志记录器和处理器
logger = None
console = None


def init_logging(log_data):
    dirname, log_name, log_name_format, log_level, log_format = log_data
    global logger, console

    if logger is not None:
        return  # 如果已经初始化，直接返回

    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    log_path = os.path.join(root_path, dirname)
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # 定义日志位置和文件名
    logname = os.path.join(log_path, log_name.format(time.strftime(log_name_format)))
    # 创建一个日志记录器
    logger = logging.getLogger('log')
    # 设置日志打印的级别
    logger.setLevel(log_level)
    # 创建日志输入的格式
    formater = logging.Formatter(log_format)
    # 创建日志处理器，用来存放日志文件
    filelogger = logging.FileHandler(logname, mode='a', encoding="UTF-8")
    # 创建日志处理器，在控制台打印
    console = logging.StreamHandler()
    # 设置控制台打印日志界别
    console.setLevel(log_level)
    # 文件存放日志级别
    filelogger.setLevel(log_level)
    # 文件存放日志格式
    filelogger.setFormatter(formater)
    # 控制台打印日志格式
    console.setFormatter(formater)
    # 将日志输出渠道添加到日志收集器中
    logger.addHandler(filelogger)
    logger.addHandler(console)


def log_info(message):
    if logger is not None:
        logger.info(message)  # 记录日志信息


# 定义日志开启关闭
def disable_log(disable_logging, data):
    if disable_logging:
        init_logging(data)  # 确保日志记录器和处理器已经初始化
    else:
        if logger is not None:
            logger.disabled = True  # 禁用日志记录器


# 定义计算当前时间-文件创建时间是否大于超时时间
def clear_logs(expiration_hours):
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_path = os.path.join(current_dir, "log")
    current_time = datetime.now()
    if os.path.exists(log_path):
        for filename in os.listdir(log_path):
            file_path = os.path.join(log_path,filename)
            if os.path.isfile(file_path):
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                time_difference = current_time - file_mtime
                if time_difference > timedelta(hours=expiration_hours):
                    os.remove(file_path)
    else:
        pass
