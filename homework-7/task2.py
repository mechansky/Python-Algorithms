"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import timeit
import operator
import random


def merge_sort(lst, compare=operator.lt):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = int(len(lst) / 2)
        left = merge_sort(lst[:middle], compare)
        right = merge_sort(lst[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(f'массив из 10 элементов: ',
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(f'массив из 100 элементов: ',
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(f'массив из 1000 элементов: ',
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))


# нашел такой вариант, который также основан на слиянии
# от вашего отличается тем, что используется здесь функции поделены на две, первая раскладывает на отдельные массивы
# вторая - функция слияния. принцип такой же, исполнено чуть иначе
# P.S. очень сложная тема, пока сам стараюсь разобраться, как конкретно работает слияние