# 解决了参数在一个线程中各个函数之间互相传递的问题
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local() # 全局变量

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(itname):
    # 绑定ThreadLocal的student:
    local_school.student = itname # 每个属性如local_school.student都是线程的局部变量
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()