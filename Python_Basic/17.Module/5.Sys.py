import sys

sys.argv          # 在终端运行时，命令行参数List，第一个元素是程序本身路径，第二个可以传参数 python3 file.py post 就会返回一个列表，[0]为路径,[1]就为post
sys.exit(n)       # 在终端运行时，退出程序，正常退出时exit(0)
sys.version       # 获取Python解释程序的版本信息
sys.maxint        # 最大的Int值
sys.path          # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform      # 返回操作系统平台名称
sys.module[__name__ ] # 得到当前模块对象

# 进度条
import time
for i in range(100):
    sys.stdout.write('#') # 输出，会将内容放入缓存，再一起输出，print就是在其基础上写的
    time.sleep(0.1)
    sys.stdout.flush() # 每次刷新
