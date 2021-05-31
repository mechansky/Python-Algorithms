"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from collections import deque
from timeit import timeit
import random

lst1 = list(range(1, 21))
print(lst1)

lst2 = deque(range(1, 21))
print(lst2)

def lst_add(lst):
    for element in range(1, 1000):
        lst.append(element)

def lst_ins(lst):
    for element in range(1, 10):
        lst.insert(0, element)

def deq_leftappend(lst):
    for element in range(1, 10):
        lst.appendleft(element)

def lst_rand(lst):
    return random.choices(lst, k=100)

print(
    f'append листа: ',
    timeit(
        "lst_add(lst1)",
        setup='from __main__ import lst_add, lst1',
        number=10000))

print(
    f'insert листа: ',
    timeit(
        "lst_ins(lst1)",
        setup='from __main__ import lst_ins, lst1',
        number=100))

print(
    f'rand листа: ',
    timeit(
        "lst_rand(lst1)",
        setup='from __main__ import lst_rand, lst1',
        number=100))

print(
    f'append deque: ',
    timeit(
        "lst_add(lst2)",
        setup='from __main__ import lst_add, lst2',
        number=10000))

print(
    f'appendleft deque: ',
    timeit(
        "deq_leftappend(lst2)",
        setup='from __main__ import deq_leftappend, lst2',
        number=100))

print(
    f'rand deque: ',
    timeit(
        "lst_rand(lst2)",
        setup='from __main__ import lst_rand, lst2',
        number=100))


# как видно, заполнение элементов списка и дека происходит +/- одинаковое количество времени. если говорить об операциях
# внесения первого элемента (insert для списка и appendleft для дека, то операция для дека быстрее в РАЗЫ потому что у
# deque имеет сложность O(1), а у листа O(N)
# если же речь об обращении к случайным элементам, то скорость списка гораздо выше.

