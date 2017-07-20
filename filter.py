def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
        
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列

    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

#回文
def is_palindrome(n):
    m = int(str(n)[::-1])
    return m == n
'''
# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
'''

output = filter(is_palindrome, range(1, 1000))
print(list(output))


# sort
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=lambda i:i[0]))  #按名字排序
print(sorted(L,key=lambda i:i[1]))   #按成绩排序


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(name):
    return name[0]

def by_score(score):
    return score[1]

print(sorted(L, key=by_name))
print(sorted(L, key=by_score))
