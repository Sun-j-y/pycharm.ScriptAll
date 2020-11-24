import os
import winreg as reg

key = reg.OpenKey(reg.HKEY_CURRENT_USER, "Software\JavaSoft\Prefs\jetbrains")
i = 0

try:
    while True:
        print(reg.EnumKey(key, i))
        i += 1
except Exception as e:
    print(e)

file_path = "D:/Test"

file_list = [
    "test1.txt",
    "test2.txt",
    "test3.txt",
    "test4.txt",
    "test5.txt",
    "test6.txt",
    "test7.txt"
]
path = file_path.strip().rstrip("\\")
print(path)
if not os.path.exists(path):  # 目录不存在
    os.makedirs(path.encode("utf-8"))
    print(path + " 创建成功")
else:
    print(path + " 已经存在")
for f in file_list:
    open(path + "/" + f, "a")

reg.CreateKey(reg.HKEY_CURRENT_USER, "AAA")

reg.DeleteKey(reg.HKEY_CURRENT_USER, "AAA")
