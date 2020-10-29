"""
Jetbrains重置试用期 v0.0.1

"""
import glob
import os

# 删除注册表 计算机\HKEY_CURRENT_USER\Software\JavaSoft\Prefs 下的所有jetbrains 相关的
# 移除 C:\Users\[用户名]\AppData\Romaing\JetBrains\[软件名称版本号] 下的一些文件
#    ./eval/ 目录下所有文件
#    ./options/ 下的other.xml
from winreg import *

# Jetbrains全家桶
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


# 删除列表中的所有文件
def del_files(del_list):
    if not del_list:
        # for file in del_list:
        #     os.remove(del_list)
        #     print("删除文件: " + del_list)
        print("删除成功")
    else:
        print("待删除列表为空")


del_file_list = [
    '百度云SVIP长期免费使用.url',
    '本教程由我爱学it提供.url',
    '高清电子书籍.url',
    '更多精品教程.url',
    '下载必看.txt',
]


def deleteFiles():
    for root, dirs, files in os.walk(u'D:\\test'):  # 要批量删除文件的最上级文件夹
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name in del_file_list:
                print("-" * 20)
                print('delete:%s' % file_path)  # 查看删除文件具体路径
                os.remove(file_path)


def main():
    # 删除 eval目录下的所有文件
    for jet in Jetbrains_list:
        print(glob.glob(os.path.join("C:\\Users\\Sun-JY\\AppData\\Roaming\\JetBrains\\" + jet + "*\\eval",
                                     "*")))
    # 删除 options目录下的other.xml文件
    for jet in Jetbrains_list:
        print(glob.glob(os.path.join("C:\\Users\\Sun-JY\\AppData\\Roaming\\JetBrains\\" + jet + "*\\options",
                                     "other.xml")))
    # 删除注册表
    # DeleteKey(ConnectRegistry(None, HKEY_CURRENT_USER), r'Software\JavaSoft\Prefs\jetbrains')


if __name__ == '__main__':
    main()
