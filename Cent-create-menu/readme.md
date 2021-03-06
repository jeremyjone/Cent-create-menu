##使用说明：

**在运行之前，确保如下事情：**
* 有一个图标文件，用于菜单显示，该文件名应该为"ffm.ico"
* 所有需要执行的脚本程序均需要管理员权限，请确保当前运行环境是管理员权限

---

如果您已经做好了初始化的准备，那么可以开始运行initFFM脚本，它会帮助您：

    1. 创建一个根目录下的ffm文件夹（如果没有的话）
    2. 在ffm目录下创建一个基础log文件 base_log.log（如果没有的话）
    3. 拷贝准备好的ffm.ico到ffm文件夹下，用于菜单显示
    4. 创建一个顶级菜单，它会显示在CentOS的最上角菜单中，方便今后添加的任何菜单内容
    5. 创建菜单类别，用于将今后添加的菜单放在此类别中


---
####创建子菜单：
** 您现在应该已经运行过初始化脚本程序，所以当前您的电脑应该已经存在顶级菜单和相应配置，以及根目录下的"/ffm"目录，请确保这一点，再进行以下操作。**

您现在即将开始创建属于自己的子菜单，直接运行submenu前缀的脚本即可，不过对于不同的子菜单脚本，仍然有一些需要注意的地方：

    version_ctrl：版本管理程序，这个并不需要特别注意的地方；
    open_web：打开pipeline， 在运行这个子菜单脚本之前，需要确保当前目录下已经存在一个名为"explorer.ico"的浏览器图标（这样比较好看，也不会反逻辑），
              同时需要一个名字为"open_pipeline"的运行程序，内容为打开浏览器并且跳转到pipeline地址（linux专用）
    history: 历史管理程序，这个并不需要特别注意的地方；



####删除菜单项：

**在您确认删除之前，需要确认所有对应的菜单项已经被添加到了删除py文件的列表中，其他无需修改。**

当您确认删除，只需要启动deleteFFM即可，程序会帮助您完整的卸载已经添加的菜单项，并且将系统的冗余代码清理干净。


