# 线程和进程的关系
# 进程是资源分配的基本单位
# 线程是调度的基本单位

# 关于如何创建线程和进程

# 创建线程

# from threading import Thread

# 有两种创建方式


# 第一种方式
# def func(name):
#     for i in range(1000):
#         print(name + str(i))
#
#
# if __name__ == '__main__':
#     # 通过args进行传参
#     # 参数必须通过args进行传参，参数必须为元组，但是列表好像也行。
#     t = Thread(target=func, args=('风中奇缘', ))
#     t.start()
#
#     for i in range(100):
#         print('主线程', i)

# 第二种方式
# class MyThread(Thread):
#     # 重写Thread的run方法
#     def run(self) -> None:
#         for i in range(100):
#             print('子线程', i)
#
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()       # 这个不能直接调用run方法，如果直接调用run方法，就相当于普通的函数调用
#
#     for i in range(100):
#         print('主线程', i)

#################################################
# 以上是如果创建线程的方式
# 一下介绍一下进程的方式
from multiprocessing import Process


# 创建方式很像
# class MyProcess(Process):
#     def run(self) -> None:
#         for i in range(100):
#             print('子进程', i)
#
#
# if __name__ == '__main__':
#     p = MyProcess()
#     p.start()
#
#     for i in range(100):
#         print('主进程', i)

# def func(name):
#     for i in range(100):
#         print(name + str(i))
#
# if __name__ == '__main__':
#
#     p = Process(target=func, args=('宫灯舞', ))
#     p.start()
#
#     for i in range(100):
#         print('主进程', i)

