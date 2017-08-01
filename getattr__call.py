class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
        
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path): # 动态获取属性时返回新实例
        print("%s  %s" % (self._path, path))
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, attr): # 将新对象当函数调用时做相同操作
        return Chain('%s/:%s' % (self._path, attr))
    
    def __str__(self):
        return self._path

    __repr__ = __str__

if __name__ == "__main__":
    print(Chain().status.user('michael').timeline.list)

    s = Student('Michael')
    s() # self参数不要传入，调用实例方法时，使用s.XXX()，这里直接在实例本身上使用
    callable(Student()) # True， 判断一个对象是否是“可调用”对象
