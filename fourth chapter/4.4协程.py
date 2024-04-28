# 协程的概念
# input() 程序处在阻塞状态
# requests.get() 再网络请求返回数据前，程序也是处于阻塞状态
# 一般情况下，当程序处于 IO操作的时候，线程都会处于阻塞状态

# 协程： 当程序遇见了Io操作的时候，可以选择性的切换到其他任务上。

# 在宏观上，看到的是多个任务一起运行
# 实际上是多任务异步操作

# 以上的东西都是在单线程的条件下

# python 编写协程的程序

import time
import asyncio


# 定义为协程函数，就是在该函数中如果有阻塞状态，那么
async def func():
    print('开始func')
    print('你好，我叫御坂美琴1')
    # time.sleep(3)       # 当程序出现了同步操作的时候，异步就中断了, requests.get也会造成阻塞, 也是同步操作
    await asyncio.sleep(3)    # 异步操作的代码
    print('你好，我叫御坂美琴2')


async def func1():
    print('开始func1')
    print('你好，我叫张萌1')
    await asyncio.sleep(5)
    print('你好，我叫张萌2')


async def func2():
    print('开始func2')
    print('你好，我叫小龙女1')
    await asyncio.sleep(5)
    print('你好，我叫小龙女2')


async def func3():
    print('开始func3')
    print('你好，我叫陈秉楠1')
    await asyncio.sleep(6)
    print('你好，我叫陈秉楠2')


async def func4():
    print('开始func4')
    print('你好，我叫赵妍茄1')
    await asyncio.sleep(1)
    print('你好，我叫赵妍茄2')


# if __name__ == '__main__':
    # 异步是并行操作
    # f = func()          # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
    # f1 = func1()        # 协程程序运行需要asyncio模块支持
    # f2 = func2()
    # f3 = func3()
    # f4 = func4()
    # loop = asyncio.get_event_loop()
    # tasks = [
    #     loop.create_task(i) for i in [f, f1, f2, f3, f4]
    # ]
    #
    # t2 = time.time()
    # # 一次性启动多个任务
    # # asyncio.run(asyncio.wait(tasks))
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    # print(f'耗时: {(time.time()-t2):.2f}')

    # 同步是串行操作
    """
    func
    func1
    func2
    func3
    func4
    一共耗时20秒
    """
    # t1 = time.time()
    # func()
    # func1()
    # func2()
    # func3()
    # func4()
    # print(f'耗时: {(time.time() - t1):.2f}')


# 上面可以这么写，但是这会导致python 主线程的任务太多
# 官方希望按照下面这么写

async def main():
    # 说实话，挺蛋疼的，现在我的python 版本是3.11 协程写法早就不太一样了，我也不知道我这么写行不行
    # 第一种写法
    # 这么写不推荐
    # f = func()
    # await f     # 异步协程的调用
    # f2 = func2()
    # await f2        # 一般await挂起操作放在协程对象前面
    #####################################################
    # 第二种写法，推荐写法
    # 太好了，这么跑是可以跑通的
    # 这种写法是最多的
    tasks = [
        asyncio.create_task(i) for i in [
            func(),
            func2(),
            func3()]
    ]
    await asyncio.wait(tasks)   # 需要挂起的操作都需要这个await

if __name__ == '__main__':
    asyncio.run(main())
