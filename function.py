def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city, '\n')

'''
def add_end(L=[]):
    L.append('END')
    return  L
'''

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return  L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print('name:', name, 'age', age, 'other', kw)

def person2(name, age, *, city, job):
    print(name, age, city, job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)



enroll('张三', '男')
enroll('李四', '女', 10)
enroll('王五', '女', city='Shanghai')

print(add_end())
print(add_end())

print(calc(1,2))
num = [1,2,3]
print(calc(*num))

person('Michael', 30)
person('Michael', 30, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Michael', 30, **extra)

person2('Jack', 24, city='Beijing', job='Engineer')


args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
