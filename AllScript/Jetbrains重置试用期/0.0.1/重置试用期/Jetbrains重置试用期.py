"""
Jetbrains重置试用期 v0.0.1


"""
from __future__ import print_function

import datetime
import glob
import os
from winreg import *
import ctypes, sys

"""
操作思路    - 2020年11月7日 更新
    删除注册表 计算机\\HKEY_CURRENT_USER\\Software\\JavaSoft\\Prefs 下的所有jetbrains相关项
    移除 C:\\Users\\[用户名]\\AppData\\Romaing\\JetBrains\\[软件名称版本号]\\eval\ 目录下所有文件
    移除 C:\\Users\\[用户名]\\AppData\\Romaing\\JetBrains\\[软件名称版本号]\\options 下的other.xml文件
"""

# Jetbrains全家桶  用于匹配文件路径
Jetbrains_list = [
    'IntelliJIdea',  # Java
    'WebStorm',  # 前端
    'PyCharm',  # python
    'GoLand',  # GoLand
    'CLion',  # C&C++
    'DataGrip',  # 数据库
    'RubyMine',  # Ruby
    'AppCode',  #
    'Rider',  #
]


# 获取当前时间
def get_time(f):
    return datetime.datetime.now().strftime(f)


def write_log_file(msg):
    log_str = get_time('%Y-%m-%d %H:%M:%S') + ' - ' + msg  # 拼接要写入log的字符串
    # 根据日期打开文件 如果文件不存在则创建 将光标放在文件末尾
    log_file = open("./" + get_time('%Y-%m-%d') + ".log", mode='a', encoding='utf8')
    log_file.write(log_str + "\n")  # 写入一行数据
    log_file.close()  # 关闭文件
    return log_str  # 返回写入文件的字符串


# 日志收集
def log(msg, is_output: bool):
    if is_output:  # 是否打印到控制台
        print(write_log_file(msg))
    else:
        write_log_file(msg)


# 删除列表中的所有文件
def del_files(del_list):
    if not del_list:
        log("待删除列表为空", False)
    else:
        for f in del_list:
            os.remove(f)
            log("删除文件: " + f, True)


def main():
    # 删除 eval目录下的所有文件
    log("正在删除*/eval目录下文件...", True)
    for jet in Jetbrains_list:
        del_files(glob.glob(
            os.path.join("C:\\Users\\Sun-JY\\AppData\\Roaming\\JetBrains\\" + jet + "*\\eval", "*")))

    # 删除 options目录下的other.xml文件
    log("正在删除*/option/other.xml文件...", True)
    for jet in Jetbrains_list:
        del_files(glob.glob(
            os.path.join("C:\\Users\\Sun-JY\\AppData\\Roaming\\JetBrains\\" + jet + "*\\options", "other.xml")))

    # 删除注册表
    log("正在删除注册表jetbrains相关项...", True)
    # DeleteValue(HKEY_CURRENT_USER, r'Software\JavaSoft\Prefs\jetbrains')
    DeleteKey(ConnectRegistry(None, HKEY_CURRENT_USER), r'Software\JavaSoft\Prefs\jetbrains')
    log("操作完成", True)
    input("\n输入任意键继续...")
    # os.system('pause')


def admin_exec():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception as e:
            return False

    if is_admin():  # 将要运行的代码加到这里
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        # 如果您使用的是Python 2.x，那么您应该替换这一行：
        # ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


if __name__ == '__main__':
    main()
