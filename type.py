def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

# type 动态创建类
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
# 第二个参数支持父类多继承，(object,)为tuple的单元素写法

h = Hello()
h.hello()
print(type(Hello))
print(type(h))


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value) # 加上add方法
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass): # 指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
    pass

L = MyList()
L.add(1)
print(L)
