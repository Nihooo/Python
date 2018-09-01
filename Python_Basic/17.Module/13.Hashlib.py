# hashlib模块 摘要算法，将明文转变为密文，但不能从密文转换为明文,主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
import hashlib

# obj = hashlib.md5() # sha256、sha512
# obj = hashlib.md5("aaa".encode("utf-8")) # 加盐
# print(obj)
# obj.update("hello".encode("utf-8"))
#
# # print(obj.hexdigest())
# # print(len(obj.hexdigest())) # hash的位数不会变，32位
#
# obj.update("admin".encode("utf-8")) # 是在hello的基础上加了个admin

# print(obj.hexdigest()) # dbba06b11d94596b7169d83fed72e61b

# 等于上面
# obj.update("helloadmin".encode("utf-8"))
# print(obj.hexdigest()) # dbba06b11d94596b7169d83fed72e61b
