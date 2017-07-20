当语句以冒号:结尾时，缩进的语句视为代码块
a = 100
if a >= 0:
    print(a)
else:
    print(-a)


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
切片也可用于字符创串，操作结果仍是字符串

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
