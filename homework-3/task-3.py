"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)
"""

user_input = input('Введите строчные латинские буквы: ')
a = 0
c = len(user_input)
substrings = []
substring_hashes = []

while a + 1 != len(user_input):
    substrings.append(user_input[a:a + 1])
    substrings.append(user_input[a:])
    substrings.append(user_input[:c])
    substrings.append(user_input[a:c])
    a += 1
    c -= 1
    if '' in substrings:
        substrings.remove('')
    if user_input in substrings:
        substrings.remove(user_input)


for element in substrings:
    substring_hashes.append(hash(element))
    substring_hashes_unique = set(substring_hashes)


print(f'Количество уникальных подстрок в строке {user_input}: {len(substring_hashes_unique)}')