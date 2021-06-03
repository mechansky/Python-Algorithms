import memory_profiler
import copy
from sys import getrefcount
from timeit import default_timer, timeit
import random
from collections import namedtuple


def analyze(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper



@analyze
def less_than_number_1(numbers):
    lst = [element for element in numbers]
    return lst




@analyze
def less_than_number_2(numbers):
    for element in numbers:
        yield element



if __name__ == '__main__':
    res, mem_diff = less_than_number_1(list(range(1000)))
    print(f'выполнение со списком заняло {mem_diff} Mib')


if __name__ == '__main__':
    my_generator, mem_diff = less_than_number_2(list(range(1000)))
    print(type(my_generator))
    for i in my_generator:
        print(i)
    print(f'выполнение с генератором заняло {mem_diff} Mib')


# здесь, как и аналогично примеру с урока, используется генератор во втором случае для вывода всех чисел менее указываемого
# в случае с генератором, числа менее задаваемого не хранятся в памяти, соответственно операция занимает гораздо меньше памяти
# в случае же с итераторами, затрачивается память на хранение чисел
