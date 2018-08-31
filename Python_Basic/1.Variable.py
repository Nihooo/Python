# utf-8用三个字节表示中文，24位：GBK用两个字节表示

print("hello world")

'''
name = input("请输入用户名:")
passwd = input("请输入密码:")
if name == "root":
  if passwd == "123"
    print("welcome, %s" % name)
  else:
    print("密码错误")
elif name == "alex":
  print("get out")
elif name == "wpq":
  pass
else:
  print("用户名错误")
'''

# 逐层退出与一次性退出
tag = True
while tag:
  print("level1")
  choice = input("level>>:").strip()
  if choice == "quit":
    break
  if choice == "quit_all":
    tag = False
  while tag:
    print("level2")
    choice = input("level2>>:").strip()
    if choice == "quit":
      break
    if choice == "quit_all":
      tag = False
    while tag:
      print("level3")
      choice = input("level3>>:").strip()
      if choice == "quit":
        break
      if choice == "quit_all":
        tag = False
        
