import os

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
newPath = os.path.join(os.path.abspath('.'), 'testdir')
# 由于Linux/Unix/Mac下使用'/'路径分隔符，Windows下使用'\'路径分隔符，所以使用os.path.join
# 同样拆分路径使用os.path.split('/Users/michael/testdir/file.txt')，返回('/Users/michael/testdir', 'file.txt')
print(newPath)
# 然后创建一个目录:
os.mkdir(newPath)
# 删掉一个目录:
os.rmdir(newPath)

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
