#-*- coding:utf-8 -*-
"""
Initialize FFM Pipeline software in Linux.

Script will do something:
    1. create base log file named "base_log.log" in "/ffm" path,
       if this path not exist, this script will be created.
    2. copy "ffm.ico" to "/ffm" path, so make sure you have this
       icon file in this folder before running this script.
    3. script will create top level menu named "FFM Pipeline",
       for show submenus in menu.
    4. script will create one menu category named "FFM", to make
       it easy to add submenus in the future.
"""
__author__ = 'jeremyjone'
__datetime__ = '2018-09-21 14:20'


import os

from util import config
import create_top_directory, create_menu_category


def createLogfile():
    if not os.path.exists(config.FFM_PATH):
        os.system("mkdir %s" % config.FFM_PATH)
    if not os.path.exists(os.path.join(config.FFM_PATH, config.LOG_BASE_FILE_NAME)):
        os.system("touch %s" % os.path.join(config.FFM_PATH, config.LOG_BASE_FILE_NAME))
    os.system("chmod 777 %s" % os.path.join(config.FFM_PATH, config.LOG_BASE_FILE_NAME))


def run():
    createLogfile()
    os.system("cp ./ffm.ico /ffm")
    create_top_directory.run()
    create_menu_category.run()



if __name__ == '__main__':
    run()
