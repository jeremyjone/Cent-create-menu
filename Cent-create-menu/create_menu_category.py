#-*- coding:utf-8 -*-
"""
This script is used to create menu categories for future submenu categories.
"""
__author__ = 'jeremyjone'
__datetime__ = '2018-08-10 12:11'

import os, re
from util import log


ffm_menu = '''
  <!-- FFM -->
  <Menu>
    <Name>FFM</Name>
    <Directory>FFM.directory</Directory>
    <OnlyUnallocated/>
    <Include>
      <And>
        <Category>FFM</Category>
      </And>
    </Include>
  </Menu> <!-- End FFM -->
'''


sub_other = '''
<!-- Other -->
  <Menu>
    <Name>Other</Name>
    <Directory>X-GNOME-Other.directory</Directory>
    <OnlyUnallocated/>
    <Include>
      <And>
        <Category>Other</Category>
        <Not><Category>Core</Category></Not>
        <Not><Category>Settings</Category></Not>
        <Not><Category>SystemSetup</Category></Not>
        <Not><Category>X-Red-Hat-ServerConfig</Category></Not>
        <Not><Category>Screensaver</Category></Not>
        <Not><Category>Documentation</Category></Not>
      </And>
    </Include>
  </Menu> <!-- End Other -->
'''

menu_name = "applications.menu"
menu_path = "/etc/xdg/menus/"


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
    file_content = _readFile(menu_path + menu_name)
    if re.findall(r"<!-- FFM -->", file_content):
        return ""
    parttern = re.compile(r'<!-- Other -->[\s\S]*<!-- End Other -->')
    a = re.findall(parttern, file_content)
    if a:
        sub_file = file_content.replace(a[0], sub_other + ffm_menu)
    else:
        return ""
    return sub_file


def createMenu():
    file_content = menuHandler()
    if file_content != "":
        _createFile(menu_path, menu_name, file_content)
    else:
        log.logger.warning("Menu file has FFM item.")


def run():
    createMenu()


if __name__ == '__main__':
    run()


