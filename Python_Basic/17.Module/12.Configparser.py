# configparser模块 配置解析

import configparser

# 创建配置文件
'''
config = configparser.ConfigParser() # 实例化对象config={}

config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here


with open('example.ini', 'w') as f:
    config.write(f)
'''


# 配置文件的增删改查

import configparser

# config = configparser.ConfigParser()

# config.read('example.ini') # 读文件

# print(config.sections()) # 打印块名

# print(config['bitbucket.org']['User']) # 不区分大小写
# print(config['DEFAULT']['Compression'])

# for i in config['bitbucket.org']: # 会将default的内容默认遍历出来
#      print(i)

# print(config.options('bitbucket.org')) # 取'bitbucket.org'里的key，相当于上面的for，但会放在一个列表里

# print(config.items('bitbucket.org')) # 取键值

# print(config.get('bitbucket.org', 'compression')) # 取值

# 增加块
# config.add_section('alex')
# config.set('alex', 'k1', '111') # 在块中增加键和值
# config.write(open('example.ini', 'w')) # 将修改内容重新写入


# 删除键和值
#config.remove_option('alex', 'k1')
# config.remove_section('alex') # 删除块
# config.write(open('example.ini', 'w'))
