"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_upgraded(lst_obj):
    n = 1
    x = 0
    if sorted(lst_obj, reverse=True) == lst_obj:
        return lst_obj
    else:
        while n < len(lst_obj) - x:
            for i in range(len(lst_obj) - n):
                if lst_obj[i] < lst_obj[i + 1]:
                    lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
            n += 1
            x += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(100)]
sorted_list = [element for element in sorted(range(1, 101), reverse=True)]

bubble_sort(orig_list[:])
bubble_sort(sorted_list[:])


bubble_sort_upgraded(orig_list[:])
bubble_sort_upgraded(sorted_list[:])


print(f'замеры список из 100 неотсортированных элементов с помощью bubble_sort: ',
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(f'замеры список из 100 отсортированных элементов с помощью bubble_sort: ',
    timeit.timeit(
        "bubble_sort(sorted_list[:])",
        globals=globals(),
        number=1000))

print(f'замеры список из 100 неотсортированных элементов с помощью bubble_sort_upgraded: ',
    timeit.timeit(
        "bubble_sort_upgraded(orig_list[:])",
        globals=globals(),
        number=1000))

print(f'замеры список из 100 отсортированных элементов с помощью bubble_sort_upgraded: ',
    timeit.timeit(
        "bubble_sort_upgraded(sorted_list[:])",
        globals=globals(),
        number=1000))

# соответственно, в функции upgraded с помощью переменной "x" мы пришли к тому, что часть отсортированных элементов
# не будет проверяться повторно, что ускоряет выполнение функции с 1.36 до 1.11 с.
# также я добавил проверку, если список уже отсортирован, что ускоряет работу функции, если мы пытаемся отсортировать
# уже отсортированный массив

