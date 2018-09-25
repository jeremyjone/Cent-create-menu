#-*- coding:utf-8 -*-
"""
Create history menu.
"""
__author__ = 'jeremyjone'
__datetime__ = '2018-09-21 15:48'


import sys, os
from util import log, config


desktop_path = "/usr/share/applications/"
desktop_name = "ffm-history.desktop"
menu_name = "FFM History"

desktop = '''
[Desktop Entry]
Name={0}
GenericName={1}
Comment={2}
Exec={3} %u
Icon={4}
Terminal=false
StartupNotify=true
Type=Application
Categories=FFM;
X-Desktop-File-Install-Version=0.15
'''.format(menu_name, menu_name, menu_name,
           config.HISTORY_START_FILE,
           os.path.join(config.FFM_PATH, config.ICON_FFM))



def createFile(path, name, content):
    if not os.path.exists(os.path.join(path, name)):
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, name), 'wb') as f:
            f.write(content)
    else:
        log.logger.warning("Desktop file exists, can not create %s" % desktop_name)


def createDesktop():
    createFile(desktop_path, desktop_name, desktop)
    os.system('update-desktop-database')


def createLogfile():
    log_path = config.FFM_PATH
    log_name = config.LOG_HISTORY_FILE_NAME
    if not os.path.exists(log_path):
        os.system("mkdir %s" % log_path)
    if not os.path.exists(os.path.join(log_path, log_name)):
        os.system("touch %s" % os.path.join(log_path, log_name))
    os.system("chmod 777 %s" % os.path.join(log_path, log_name))


def run():
    createLogfile()
    createDesktop()


if __name__ == '__main__':
    if 'win' in sys.platform:
        pass
    else:
        run()