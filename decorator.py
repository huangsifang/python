import functools
'''
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw): #可接受任意参数
        print('call %s():' % func.__name__) #函数对象有一个__name__属性，可以拿到函数名字
        return func(*args, **kw)
    return wrapper

@log #相当于now = log(now)
def now():
    print('2015-3-25')

f = now
f()
'''
'''
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute') #相当于now2 = log2('execute')(now2)
def now2():
    print('2015-3-25')

now2()
'''
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator(func=text) if callable(text) else decorator #若没有参数，text为func可调用，则if成立

@log('execute')
def now():
    print('2015-3-25')

@log
def now2():
    print('2015-3-25')

now()
now2()
