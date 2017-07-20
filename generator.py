'''
def triangles(max):
    n = 0
    L = [1,]
    while n < max:
        L2 = [1,]
        count = 1
        while count<n:
            L2.append(L[count-1]+L[count])
            count = count+1
        if n!= 0:
            L2.append(1)
        L = L2.copy()
        yield L2
        n = n + 1
    return 'done'

g = triangles(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''
def tri():
    L=[1]
    yield L
    while True:
        L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]
        yield L

n=0
for L in tri():
    print(L)
    n=n+1
    if n==10:
        break
