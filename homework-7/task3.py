"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
"""

import random

m = int(input('введите число m в формуле (2*m) + 1: '))

orig_list = [random.randint(-100, 100) for _ in range((2*m)+1)]
print(f'список: {orig_list}')
n = 1
while n < len(orig_list):
    orig_list.pop(orig_list.index(max(orig_list)))
    n += 1

print(f'медиана списка составляет: {max(orig_list)}')



