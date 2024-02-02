import functools
import time


def f_time(func=None, *, n_iter=10):
    if func is None:
        return lambda func: f_time(func, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, end="...")
        acc = float("inf")
        for i in range(n_iter):
            start = time.perf_counter()
            res = func(*args, *kwargs)
            acc = min(acc, time.perf_counter() - start)
        print(f"{acc:.6f}")
        return res

    return inner


def square(a):
    return a**2


@f_time
def listcomp(lst):
    return [i**9 for i in lst][9]


@f_time
def map_(lst):
    for i in range(9):
        res = next(map(lambda x: x**9, lst))
    return res


lst = list(range(999))
listcomp(lst)
map_(lst)


def retry(func=None, ret=2):
    # со скобками
    if func is None:
        return lambda func: retry(func, ret=ret)

    # без
    def inner(*args, **kwargs):
        for r in range(ret):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
            else:
                break

    return inner


# @retry
def division():
    num1 = int(input("1: "))
    num2 = int(input("2: "))
    print(num1 / num2)


# retry(division, ret=1)()
