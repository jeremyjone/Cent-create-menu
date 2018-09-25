#-*- coding:utf-8 -*-
"""
Create open web Pipeline menu, click this menu will
jump to pipeline intranet.

This script need program for start, user need prepare
a program named "open_pipeline" and one icon named
"explorer.ico" save in "/ffm" folder.

"""
__author__ = 'jeremyjone'
__datetime__ = '2018-09-21 15:25'

import sys, os
from util import log, config


desktop_path = "/usr/share/applications/"
desktop_name = "ffm-open-pipeline.desktop"
menu_name = "FFM Pipeline Web"

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
           os.path.join(config.FFM_PATH, config.OPEN_PIPELINE_WEB_FILE),
           os.path.join(config.FFM_PATH, config.ICON_EXPLORER))



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



def run():
    os.system("cp ./open_pipeline /ffm")
    os.system("chmod 777 /ffm/open_pipeline")
    os.system("cp ./explorer.ico /ffm")
    createDesktop()


if __name__ == '__main__':
    if 'win' in sys.platform:
        pass
    else:
        run()