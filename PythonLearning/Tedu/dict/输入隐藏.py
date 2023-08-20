import getpass  # 隐藏输入
import hashlib  # 转换加密

# 输入隐藏
pwd = getpass.getpass("PW: ")
print(pwd)

# 算法加盐 (#$awv3)
# abc123#$awv3

# hash对象
hsh = hashlib.md5('*#06L_'.encode())  # 生成对象
hsh.update(pwd.encode())  # 算法加密
pwd = hsh.hexdigest()  # 提取加密后的密码
print(pwd)