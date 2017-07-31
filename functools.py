import functools
int2 = functools.partial(int, base=2) # 相当于kw={'base':2}  int('10010', **kw)
print(int2('1000000'))
print(int2('1010101'))


max2 = functools.partial(max, 10)
print(max2(5, 6, 7))  # 相当于args = (10, 5, 6, 7)  max(*args)
