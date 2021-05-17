"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

companies = {
    'Gazprom': 250000,
    'Rosneft': 350000,
    'Lukoil': 200000,
    'Yandex': 120000
}


def get_max_profit(dict):  # сложность: O(N)
    max_profit = 0  # O(1)
    for k, v in dict.items():  # O(N)
        if dict[k] > max_profit:  # O(1)
            max_profit = dict[k]  # O(1)
    print(max_profit)


get_max_profit(companies)


def get_max_profit_2(dict):  # O(N)
    lst = []  # O(1)
    for k, v in dict.items():  # O(N)
        lst.append(dict[k])  # O(1)
    max_profit = max(lst)  # O(N)
    print(max_profit)


get_max_profit_2(companies)


def get_max_profit_3(dict):  # O(N)
    lst = []  # O(1)
    for k, v in dict.items():  # O(N)
        lst.append(dict[k])  # O(1)
    lst.sort()  # O(NlogN)
    print(lst[-1])  # O(1)


get_max_profit_3(companies)


def get_max_profit_4(dict):  # O(N)
    lst = list(dict.values())  # O(N)
    max_profit = max(lst)  # O(1)
    print(max_profit) # O(1)

get_max_profit_4(companies)

#  по-моему мнению, наиболее эффективная функция здесь - get_max_profit_4 - так как при прочих равных (в функции 2 и 3
# я также думаю что O(N)), в функции 4 всего 3 строчки
