#-*- coding:utf-8 -*-
"""
This is a template for create submenu in CentOS.

* Attention: *
Before you use this script, make sure you already have
corresponding directory and categories in the CentOS.

See other templates for related creation methods.

* Method of used: *
Between " # ------- " content is editable, of course,
changes can be made elsewhere, but we do not recommend
that you do so. Unless you are already familiar with the
system.

"""
__author__ = 'jeremyjone'
__datetime__ = '2018-09-21 15:49'


import sys, os
from util import log


desktop_path = "/usr/share/applications/"

# ------------------
desktop_name = "_____menu file name________.desktop"
menu_name = "_____menu name________"


desktop = '''
[Desktop Entry]
Name={}
GenericName={}
Comment={}
Exec={} %u
Icon={}
Terminal=false
StartupNotify=true
Type=Application
Categories=FFM;
X-Desktop-File-Install-Version=0.15
'''.format(menu_name, menu_name, menu_name,
           "______file full path_______",
           "______file icon full path_______")

# ------------------

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

    # ---------------------

    log_path = "_____log file path______"
    log_name = "_____log file name______"

    # ---------------------

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