#-*- coding:utf-8 -*-
"""
Delete FFM menu in Linux.

Delete FFM menu and clean up other menu data.

When a new menu file is added, you simply add the address to the list.
"""
__author__ = 'jeremyjone'
__datetime__ = '2018-08-10 18:24'

import sys, os, re
from util import log


menu_name = "applications.menu"
menu_path = "/etc/xdg/menus"


directory = "/usr/share/desktop-directories/FFM.directory"
desktop = "/usr/share/applications/ffm-version-control.desktop"
web = "/usr/share/applications/ffm-open-pipeline.desktop"
history = "/usr/share/applications/ffm-history.desktop"

delete_file_list = [directory, desktop, web, history]



def _createFile(path, name, content):
    if not os.path.exists(path + name):
        if not os.path.exists(path):
            os.makedirs(path)

    with open(path + name, 'wb') as f:
        f.write(content)


def _readFile(file):
    with open(file, "rb") as f:
        content = f.read()
    return content


def menuHandler():
    file_content = _readFile(os.path.join(menu_path, menu_name))
    parttern = re.compile(r'<!-- FFM -->[\s\S]*<!-- End FFM -->')
    a = re.findall(parttern, file_content)
    if a:
        sub_file = file_content.replace(a[0], "")
        return sub_file
    else:
        return ""


def createMenu():
    file_content = menuHandler()
    if file_content != "":
        _createFile(menu_path, menu_name, file_content)
    else:
        log.logger.warning("Menu file don't have FFM item.")



def run():
    for f in delete_file_list:
        os.system("rm -rf %s" % f)
    createMenu()



if __name__ == '__main__':
    run()