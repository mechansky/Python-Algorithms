"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(
    timeit(
        "func_1([1, 2, 4, 6])",
        setup="from __main__ import func_1",
        number=100000
    ))

def func_2(nums):
    new_arr = [element for element in range(len(nums)) if nums[element] % 2 == 0]
    # сделал через list comprehension, поскольку эта операция быстрее, чем append
    return new_arr


print(
    timeit(
        "func_2([1, 2, 4, 6])",
        setup="from __main__ import func_2",
        number=100000
    ))
