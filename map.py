from functools import reduce
def normalize(str):
    str = str.lower()
    str = str.capitalize()
    return str

def f(x, y):
    return x*y

def prod(L):
    return reduce(f, L)

global flag, count
flag, count = 1, 0
def fn(x, y):
    global flag,count
    if y == -1:
        flag = 0
        return x
    elif flag:
        return x*10+y
    else:
        count = count+1
        return x+y*pow(0.1, count)

def char2num(s):
     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}[s]

def str2float(s):
    return reduce(fn, map(char2num, s))

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print('str2float(\'123.456\') =', str2float('123.456'))
