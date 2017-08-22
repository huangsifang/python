def consumer(): # consumer函数是一个generator
    r = ''
    while True:
        n = yield r # consumer通过yield拿到消息
        if not n: # n为空时结束
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK' # 通过yield把结果传回

def produce(c):
    c.send(None) # 启动生成器
    # 或c.next() # 触发生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 切换到consumer执行，将n的值赋值给yield表达式，返回r
        # produce拿到consumer处理的结果，继续生产下一条消息
        print('[PRODUCER] Consumer return: %s' % r)
    c.close() # 通过c.close()关闭consumer，整个过程结束

c = consumer()
produce(c) # 把一个consumer传入produce