import shelve

# 存
f = shelve.open(r'shelve') # 目的：将一个字典放入文本,会自动生成3个文件用于存放数据

f["stu1_info"] = {'name': 'alex', 'age': '18'} # 相当于字典里面存字典f = {} f['name'] = 'alvin' f['stu1_info'] = {'name': 'alex', 'age': '18'}
f["stu2_info"] = {'name': 'alvin', 'age': '20'}
f.close()

# 取
f = shelve.open(r'shelve')
print(f.get('stu1_info')['name'], type(f.get('stu1_info')))
