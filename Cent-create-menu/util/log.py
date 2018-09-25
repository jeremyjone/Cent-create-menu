#-*- coding:utf-8 -*-
"""
Script log py
"""
__author__ = 'jeremyjone'
__datetime__ = '2018-07-24 16:42'

import logging
import sys, os

import config


# 创建日志的实例
logger = logging.getLogger("logger")
# 指定Logger的输出格式
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
# 创建日志：
# 文件日志
file_handler = logging.FileHandler(os.path.join(config.FFM_PATH, config.LOG_BASE_FILE_NAME))
file_handler.setFormatter(formatter)
# 终端日志
consle_handler = logging.StreamHandler(sys.stdout)
consle_handler.setFormatter(formatter)
# 设置默认的日志级别
logger.setLevel(logging.WARNING)
# 把文件日志和终端日志添加到日志处理器中
logger.addHandler(file_handler)
logger.addHandler(consle_handler)


if __name__ == '__main__':
    pass
