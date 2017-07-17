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

元组tuple：
classmates = ('Michael', 'Bob', 'Tracy')

tuple一旦初始化就不能修改

t = (1)  表示只有一个元素的tuple t[0]不存在
t = (1,)  表示tuple中有一个1元素 t[0] == 1

t = ('a', 'b', ['A', 'B']) 其中['A', 'B']可变
若不允许改变，则t = ('a', 'b', （'A', 'B'）)

把str转换成整数  int()函数

