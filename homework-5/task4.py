"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit
import random



def dict_input(d):
    for element in range(1, 10000):
        d[element] = element

def d_rand(d):
    for element in range(1, 500):
        return d[element]


d = {}

d1 = OrderedDict({})

print(
    f'заполнение словаря: ',
    timeit(
        "dict_input(d)",
        setup='from __main__ import dict_input, d',
        number=1000))

print(
    f'получение rand элементов словаря: ',
    timeit(
        "d_rand(d)",
        setup='from __main__ import d_rand, d',
        number=1000))

print(
    f'заполнение OrderedDict: ',
    timeit(
        "dict_input(d1)",
        setup='from __main__ import dict_input, d1',
        number=1000))

print(
    f'получение rand элементов OrderedDict: ',
    timeit(
        "d_rand(d1)",
        setup='from __main__ import d_rand, d1',
        number=1000))


# в обычных операциях скорость у словарей и ordereddict одинакова, с учетом того, что с питона 3.6 словари упорядочены
# по умолчанию, думаю, OrderedDict использовать смысла не имеет.



