python 大小写敏感


r''表示''内部的字符串默认不转义
print(r'\\\t\\')


Python允许用'''...'''的格式表示多行内容
print('''line1
... line2
... line3''')
多行字符串'''...'''还可以在前面加上r使用
print(r'''\t
... \n
... \\''')

与运算 and
或运算 or
非运算 not

空值是Python里一个特殊的值，用None表示。
None不能理解为0


//除法（地板除）只取结果的整数部分


ASCII 表示大小写字母、数字和一些符号
GB2312 编进中文
Unicode把所有语言都统一到一套编码里（多一倍字节）
为方便存储和传输，UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，英文字母（1个字节），汉字（3个字节），生僻的字符才会（4-6个字节）
	在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

	用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件


ord()函数   获取字符的整数表示，只能写字符 ord('0')==48
chr()函数   把编码转换为对应的字符，只能写数字 chr(48)=='0'


对bytes类型的数据用带b前缀的单引号或双引号表示
字符串类型  'ABC'  以Unicode表示  一个字符对应若干个字节
bytes类型  b'ABC' 以ASCII表示  每个字符都只占用一个字节

encode()方法：以Unicode表示的str --> bytes
'ABC'.encode('ascii')
	b'ABC'
'ABC'.encode('utf-8')
	b'ABC'
'中文'.encode('utf-8')
	b'\xe4\xb8\xad\xe6\x96\x87'
'中文'.encode('ascii')
	报错

decode()方法：bytes --> 以Unicode表示的str


len()函数:计算str包含多少个字符
用len()函数可以获得list（列表）元素的个数


%运算符就是用来格式化字符串的
'Hi, %s, you have $%d.' % ('Michael', 1000000)
	'Hi, Michael, you have $1000000.'

%2d  占2位，不够左空
%-2d  占2位，不够右空
%02d  占两位，不够左补0
%-02d  同  %-2d
'%0*d' % (n, a) n表示位数，a表示数值

用%%来表示一个%


列表list：
classmates = ['Michael', 'Bob', 'Tracy']

获取列表最后一个元素
classmates[len(classmates) - 1]
或classmates[-1]

classmates[-2]  获取倒数第二个元素

列表操作：
追加元素到末尾  append
插入到指定位置  insert(i, 'XXX')
删除末尾元素  pop
删除指定位置元素  pop(i)
排序  sore()

元组tuple：
classmates = ('Michael', 'Bob', 'Tracy')

tuple一旦初始化就不能修改

t = (1)  表示只有一个元素的tuple t[0]不存在
t = (1,)  表示tuple中有一个1元素 t[0] == 1

t = ('a', 'b', ['A', 'B']) 其中['A', 'B']可变
若不允许改变，则t = ('a', 'b', （'A', 'B'）)

把str转换成整数  int()函数

循环
for X in XXX:
	print(x);

list(range(5))
生产0-4之间的整数[0, 1, 2, 3, 4]

for x in range(101):
    sum = sum + x

[L[x] for x in range(len(L))]循环整个list

dict键-值（key-value）：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
判断key是否存在： 
1.'Thomas' in d 返回False
2.d.get('Thomas') 返回None
d.get('Thomas', -1)，-1表示不存在时自定义的返回值

删除key  pop(key)，如pop('Bob')

set:
s = set([1, 2, 3])
set和dict类似，也是一组key的集合，但不存储value
在set中，没有重复的key

add(key)方法  添加元素到set中
remove(key)方法  删除元素

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
	{2, 3}

对于不可变对象，如str
>>> a = 'abc'
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'

函数：
abs()
max() min()
int()
float()
str()
bool()
hex()  将一个整数转化为十六进制数
将函数名赋给一个变量，就可以将变量当函数名使用
a=abs
a(-1)

定义函数
def my_abs(x):
使用 from 文件名 import 函数名  来导入函数

定义空函数：
def nop():
	pass #用于占位，也可以在其他语句中使用

if age>=18:
	pass #占位，类似于分号

函数返回多个值：
import math
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = x + step * math.sin(angle)
	return nx, ny #返回一个tuple

默认参数：
当存在两个重名函数
def pow(x):  和  def pow(x, n):时，
使用pow(5)，会报缺少参数错误
解决方法：def pow(x, n=2):，此时必须默认参数n在后

默认参数的坑
def add_end(L=[]):
	L.append('END')
	return  L

>>> add_end()
['END']
>>> add_end()
['END', 'END']
函数在定义时，默认参数L的值就被计算出来了
所以，默认参数必须指向不变对象
def add_end(L=None):
	if L is None:
        L = []

函数可变参数：
def calc(*numbers):
这时的numbers相当于一个tuple
调用方法：calc(1, 2)
若要传入list或tuple
num = [1,2,3]
calc(*num)

关键字参数
def person(name, age, **kw): #kw相当于一个dict
	print('name:', name, 'age', age, 'other', kw)

>>> person('Michael', 30)
name: Michael age: 30 other: {}
>>> person('Michael', 30, city='Beijing')
name: Michael age: 30 other: { 'city': 'Beijing' }
同时也可以直接传入一个dict
person('Michael', 30, **extra)

限制传入的dict：
def person(name, age, *, city, job):
调用方法：person('Michael', 30, city='Beijing', job='Enginner')
只接受city和job且必须存在
总结：
区别位置参数和关键字参数，使用*分割
参数定义顺序：必选参数、默认参数、可变参数、命名参数、关键字参数
def f1(a, b, c=0, *args, **kw):
def f2(a, b, c=0, *, d, **kw):

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
结果；a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

使用range：
print(list(range(1, 100, 2)))
[1,3,4,5,7...]

>>> r = []
>>> n = 3
>>> for i in range(n):
...     r.append(L[i])

切片（Slice）：
L[0:3]取L中0~2下标位置的值，0可省略
L[-2:]取倒数第二个~最后一个
L[:10:2]前10个数，每两个取一个
L[::5]所有数，每5个取一个
L[:]所有，复制一个list
切片也可用于tuple，操作结果仍是tuple
切片也可用于字符串，操作结果仍是字符串

迭代：
dict迭代的是key  for key in d:
若要迭代value  for value in d.values():
若要同时迭代key和value  for k,v in d.items():


若要实现下标迭代（enumerable函数）：
for i, value in enumerable(['A', 'B', 'C']);

>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)

列表生成式
[x * x for x in range(1, 11)]
[x * x for x in range(1, 11)if x % 2 == 0]

两层循环： [m + n for m in 'ABC' for n in 'XYZ']

列出当前目录下的所有文件和目录名：
>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

把一个list中所有的字符串变成小写：[s.lower() for s in L]
对于L = ['Hello', 'World', 18, 'Apple', None]
[x.lower() if isinstance(x, str) else x for x in L1]

在Python中，这种一边循环一边计算的机制，称为生成器：generator
创建generator：g = (x * x for x in range(10))
迭代：
for n in g:
	print(n)

使用函数定义generator：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  #包含yield关键字，就是generator
        a, b = b, a + b
        n = n + 1
    return 'done'

	其中a, b = b, a + b
	相当于：

	t = (b, a + b) # t是一个tuple
	a = t[0]
	b = t[1]

generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

循环自定义的generator函数
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break

参数类型检查  isinstance
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')

凡是可作用于for循环的对象都是Iterable类型
凡是可作用于next()函数的对象都是Iterator类型（生成器）
Python的for循环本质上就是通过不断调用next()函数实现的

判断对象是否可迭代（通过collections模块的Iterable类型判断）：
from collections import Iterable
isinstance('abc', Iterale) #返回True，表示字符串'abc'可迭代
isinstance('abc', str)#判断是否为字符串
isinstance((x for x in range(10)), Intrator)判断是否是Iterator对象(生成器是）
把list、dict、str等Iterable变成Iterator可以使用iter()函数
isinstance(iter('abc'), Iterator)

isinstance(xxx, list)
isinstance(xxx, Animal) #自定义的类

map:
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]) #r是一个Iterator
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]


>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']

reduce：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

filter:返回一个Iterator
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

去除空字符串
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

排序sort:
sorted([36, 5, -12, 9, -21])
sorted([36, 5, -12, 9, -21], key=abs)//按绝对值大小排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)//忽略大小写排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)//反向排序

关键字lambda表示匿名函数
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]

lambda x: x * x实际上就是：
def f(x):
    return x * x

Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。

偏函数（functools.partial）
>>> import functools
>>> int2 = functools.partial(int, base=2)

max2 = functools.partial(max, 10)
相当于max(10, *args)

sys模块
sys模块有一个arg变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称

if __name__=='__main__': #当直接运行文件时为true，当导入该文件时为false
    test()

类似__xxx__这样的变量是特殊变量，可以被直接引用，有特殊用途，比如__author__，__name__就是特殊变量，模块定义的文档注释也可以用特殊变量__doc__访问

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等

类：
class Student(object):
    def __init__(self, name, score): #__init__方法的第一个参数永远是self，表示创建的实例本身
        self.name = name
        self.score = score

实例的变量名如果以__开头，就变成了一个私有变量（private）：如self.__name,
Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量


type:
>>>type(123)
<class 'int'>
>>> type(123)==int
True
>>> type('abc')==type('123')
True
>>> type('abc')==str
True

>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True

>>> isinstance([1, 2, 3], (list, tuple)) #判断是否是list或tuple
True

使用dir()函数：获得一个对象的所有属性和方法

len('ABC')与'ABC'.__len__()效果相同

hasattr(obj, 'x') # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
getattr(obj, 'y') # 获取属性'y'，只有在不知道对象信息的时候，我们才会去获取对象信息
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404
hasattr(obj, 'power') # 有属性'power'吗？（pow为对象方法）

实例属性和类属性
class Student(object):
    name = 'Student #类属性
    def __init__(self, name):
        self.name = name #实例属性

Student.name #类属性
s = Student()
print(s.name) #实例属性

实例方法和类方法
>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
	该实例方法只存在于该实例中，其他实例没有

>>> def set_score(self, score):
...     self.score = score
...
>>> Student.set_score = set_score
	类方法对所有实例都有效

限制类能绑定的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
限制对于子类无效

优化get  set
class Student(object):

    @property
    def score(self): # 把get方法变成属性，调用时使用s.score，实际转化成s.get_score()
        return self._score

    @score.setter
    def score(self, value): # 把set方法变成属性，调用时使用s.score=XXX，实际转化成s.set_score()
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

使用__str__():
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name

此时 print(Student('Michael'))  返回  Student object (name=Michael)
若要在不使用print情况下同样返回这种结果，使用
    __repr__ = __str__


使用__iter__():  # 使类被用于for  in循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

        但是此时不能实现下标取数

实现下标取数（切片）：__getitem__
class Fib(object):
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

__getattr__：
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score': # 使得在调用s.score时返回99，而不是报AttributeError错误，调用其他，如s.abc时返回为None
            return 99
        # 若要使在调用s.abc时报错，则主动抛出错误
        # raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

__call__: # 在实例本身上调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.


>>> callable(Student()) # 判断一个对象是否是“可调用”对象
True


枚举：
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 使用Month.Jan来引用一个常量

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 定义类
@unique # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

if __name__ == "__main__":
    print(Weekday.Mon)  # Weekday.Mon
    print(Weekday['Tue'])  # Weekday.Tue
    print(Weekday.Tue.value)  # 2
    print(day1 == Weekday.Mon) # True
    print(Weekday(1))  # Weekday.Mon
    for name, member in Weekday.__members__.items():
        print(name, '=>', member)


try:
	XXX
except Exception as e:
	logging.expection(e) #打印错误，把错误记录到日志文件里

raise主动抛出错误：
如果不带参数，就会把当前错误原样抛出
raise ValueError('invalid value: %s' % s)，valueError是自带的错误类型，也可以自定义错误

调试：
1.print()

2.assert n!= 0, #表示n!=0应该是true，若为false，则会抛出AssertionError错误
启动Python解释器时可以用-O参数来关闭assert  python -O err.py

3.logging
import logging（一条语句可以同时输出到console和文件）
logging.basicConfig(level=logging.INFO) #指定记录信息的级别，有debug,info,warning,error
n = 0
logging.info('n = %d' % n)

4.调试器pdb
python -m pdb err.py
l：查看代码
n：单步执行
p：查看变量
q：结束调试

5.pdb.set_trace()
在程序中设置断点


单元测试
self.assertEqual(a, b)
with self.assertRaises(KeyError): # 通过d['empty']访问不存在的key时，断言会抛出KeyError
	value = d['empty']


读写文件
# 读取UTF-8编码的文本文件
with open('/path/to/file', 'r') as f: # 这样写就不用写f.close了
    # 直接读
    print(f.read())

    # 按size个字节读
    read(size)

    # 按行读
    for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉


# 读取二进制文件，比如图片、视频
f = open('/Users/michael/test.jpg', 'rb')

# 读取非UTF-8编码的文本文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

# 编码不规范的文件，直接忽略
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

读写内存
写入内存：
from io import StringIO
f = StringIO()
f.write('hello')  # 返回5
f.write(' ')  # 返回1
f.write('world!')  # 返回6
print(f.getvalue()) # 返回hello world! getvalue()方法用于获得写入后的str

读内存：
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

StringIO 用于str数据
BytesIO  用于二进制数据

写：
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8')) # 将'中文'字符串用utf-8编码
print(f.getvalue())  # 返回b'\xe4\xb8\xad\xe6\x96\x87'

读：
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()  # 返回b'\xe4\xb8\xad\xe6\x96\x87'

操作文件和目录
import os
os.name # 操作系统类型
'posix'，说明是Linux、Unix或Mac OS X
'nt', 说明是Windows

操作系统类型：os.name
详细系统信息：os.uname()，但uname()在windows上不提供
环境变量：os.environ
某个环境变量的值：os.environ.get('key')
查看当前目录的绝对路径: os.path.abspath('.')
拼接路径：os.path.join(os.path.abspath('.'), 'testdir')
拆分路径：os.path.split('/Users/michael/testdir/file.txt')
创建目录: os.mkdir(newPath)
删掉目录: os.rmdir(newPath)
得到文件扩展名：os.path.splitext('/path/to/file.txt')  # 返回('/path/to/file', '.txt')
对文件重命名: os.rename('test.txt', 'test.py')
删掉文件: os.remove('test.py')

os模块补充：shutil模块
文件复制：copyfile()函数

列出当前目录下的所有目录：[x for x in os.listdir('.') if os.path.isdir(x)]
所有.py文件：[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

序列化：pickle.dumps()
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)  返回b'\x80\x03}q\x00(X\x03\x00\x00...\x00Bobq\x04u.'
# 直接写入文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

反序列化：pickle.loads()，pickle.load()
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)  # 返回{'age': 20, 'score': 88, 'name': 'Bob'}

JSON序列化：
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))  # 返回'{"age": 20, "score": 88, "name": "Bob"}'

序列化类：
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

print(json.dumps(s, default=lambda obj: obj.__dict__))
或print(json.dumps(s.__dict__)) # 讨论中看到的

JSON反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

多进程
Unix/Linux操作系统提供了一个fork()系统调用，fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回
子进程永远返回0，而父进程返回子进程的ID

pid = os.fork()
当子进程被调用时，pid为子进程ID
当子进程调用结束时，pid为0
os.getpid() 返回当前进程ID
os.getppid() 返回父进程ID

Windows下：
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    p = Process(target=run_proc, args=('test',)) # 创建子进程
    p.start() # 执行子进程
    p.join() # 等待子进程结束

进程池：
控制子进程输入输出：
进程间通信：
myMultiprocessing2.py

多线程：myThread.py

python解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁
所以Python不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
多个Python进程有各自独立的GIL锁，互不影响。

ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上
分布进程到多计算机上：task_master.py  task_work.py

正则表达式：

定长：
\d可以匹配一个数字
\w可以匹配一个字母或数字
.可以匹配任意字符
\s可以匹配一个空格（也包括Tab等空白符）

不定长：
*表示任意个字符（包括0个）
+表示至少一个字符
?表示0个或1个字符
{n}表示n个字符
{n,m}表示n-m个字符

'-'是特殊字符，在正则表达式中，要用'\'转义

用[]表示范围，如：[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线

A|B可以匹配A或B

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。

注意：py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了

使用Python的r前缀，就不用考虑转义的问题了

match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
>>> import re
>>> re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>

切分字符串：
>>> re.split(r'\s+', 'a b   c') # 根据连续的空格切分
['a', 'b', 'c']
多个条件分割：
>>> re.split(r'[\s\,]+', 'a,b, c  d')
['a', 'b', 'c', 'd']

分组：（使用小括号）
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'

贪婪匹配：
>>> re.match(r'^(\d+)(0*)$', '102300').groups()
('102300', '')

非贪婪匹配：
>>> re.match(r'^(\d+?)(0*)$', '102300').groups() # 加上？
('1023', '00')

