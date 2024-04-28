from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def func(name):             # 这个是每个线程要干的工作
    for i in range(100):
        print(name + str(i))


if __name__ == '__main__':

    with ThreadPoolExecutor(10) as tp:
        # 这里是总体任务
        for i in range(100):
            tp.submit(func, name=f'子线程{i}')

    for i in range(100):
        print('主线程', i)
