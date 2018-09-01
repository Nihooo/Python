import os

print(os.getcwd()) # 获取当前工作的目录

print(os.getcwd())
os.chdir('module_lesson') # 改变当前的工作目录
print(os.getcwd())

print(os.getcwd())
os.chdir('..')
print(os.getcwd())

os.makedirs(r'dirname1\dirname2') # 生成多层递归目录
os.removedirs('dirname1\dirname2') # 从里到外，递归删除，前提为空

os.mkdir('dirname1') # 创建目录
os.rmdir('dirname1') # 删除空目录

os.listdir('dirname') # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

os.rename('oldname', 'newname') # 重命名文件/目录

os.remove('name') #删除一个文件

print(os.stat('草稿.py')) # 查看文件属性 st_atime上一次查看时间 st_mtime上一次修改时间 st_ctime创建时间

print(os.sep) # 得到当前操作系统的路径分隔符，win为'\\',linux为'/'

print(os.linesep) # 输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"

print(os.pathsep) # 输出用于分割文件路径的字符串 win下为;,Linux下为:

print(os.name) # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

print(os.environ) # 获取系统环境变量

print(os.path.abspath(path))  # 返回path规范化的绝对路径

path = r'C:\Users\Administrator\day22\ss.py'
print(os.path.split(path) # 将path分割成目录和文件名并以元组返回

print(os.path.dirname(path))  # 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(path))  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

os.path.exists(path)  # 如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  # 如果path是绝对路径，返回True
os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  # 如果path是一个存在的目录，则返回True。否则返回False

a = r'C:\Users\Administrator'
b = 'day22\ss.py'
print(os.path.join(a, b)) # 路径拼接

os.path.getatime(path)  # 返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  # 返回path所指向的文件或者目录的最后修改时间
