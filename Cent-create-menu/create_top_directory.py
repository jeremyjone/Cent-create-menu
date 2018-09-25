#-*- coding:utf-8 -*-
"""
description
"""
__author__ = 'jeremyjone'
__datetime__ = '2018-08-10 11:54'

import os
from util import log


directory = '''
[Desktop Entry]
Name=FFM Pipeline
Comment=FFM Pipeline
Icon=/ffm/ffm.ico
Type=Directory
'''

directory_path = "/usr/share/desktop-directories/"
directory_name = "FFM.directory"


def _createFile(path, name, content):
    if not os.path.exists(path + name):
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + name, 'wb') as f:
            f.write(content)
    else:
        log.logger.warning("Directory file exists, can not create %s" % directory_name)


def createDirectory():
    _createFile(directory_path, directory_name, directory)


def run():
    createDirectory()



if __name__ == '__main__':
    run()