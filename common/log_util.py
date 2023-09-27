import logging
import os
import time

# 创建一个全局的日志记录器和处理器
logger = None
console = None


def init_logging():
    global logger, console

    if logger is not None:
        return  # 如果已经初始化，直接返回

    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    log_path = os.path.join(root_path, "log")
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # 定义日志位置和文件名
    logname = os.path.join(log_path, "{}.log".format(time.strftime("%Y-%m-%d")))
    # 创建一个日志记录器
    logger = logging.getLogger('log')
    # 设置日志打印的级别
    logger.setLevel(logging.DEBUG)
    # 创建日志输入的格式
    formater = logging.Formatter(
        '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
    # 创建日志处理器，用来存放日志文件
    filelogger = logging.FileHandler(logname, mode='a', encoding="UTF-8")
    # 创建日志处理器，在控制台打印
    console = logging.StreamHandler()
    # 设置控制台打印日志界别
    console.setLevel(logging.DEBUG)
    # 文件存放日志级别
    filelogger.setLevel(logging.DEBUG)
    # 文件存放日志格式
    filelogger.setFormatter(formater)
    # 控制台打印日志格式
    console.setFormatter(formater)
    # 将日志输出渠道添加到日志收集器中
    logger.addHandler(filelogger)
    logger.addHandler(console)


def log_info(message):
    init_logging()  # 确保日志记录器和处理器已经初始化
    # 记录日志信息
    logger.info(message)
