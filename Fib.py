class Student(object):
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__ # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串


class Fib(object):
    
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
        
    # 用于类的for...in循环
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    

    # 用于下标取出元素
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

if __name__ == "__main__":
    print(Student('Michael'))

    for n in Fib():
        print(n)

    f = Fib()
    print(f[0:5])
    print(f[:10])

    
