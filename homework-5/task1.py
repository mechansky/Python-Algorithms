"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple

FIRMS = namedtuple('Information_card', 'name incomes_1 incomes_2 incomes_3 incomes_4')
firm_list = []
amount_of_firms = int(input('введите количество фирм: '))
i = 1


def create_firm():
    data = []
    data.append(input(f"введите наименование фирма_{i}:  "))
    incomes = (list(map(int, input('через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала):  ').split())))
    firm = FIRMS._make(data + incomes)
    firm_list.append(firm)


def get_total_profit(firm):
    return firm.incomes_1 + firm.incomes_2 + firm.incomes_3 + firm.incomes_4


def get_average_profit():
    total_profit = []
    for element in firm_list:
        total_profit.append(get_total_profit(element))
    average_profit = sum(total_profit) / len(firm_list)
    return average_profit

def analyze():
    less_average = []
    above_average = []
    average = []
    for element in firm_list:
        if get_total_profit(element) > get_average_profit():
            above_average.append(element)
        elif get_total_profit(element) < get_average_profit():
            less_average.append(element)
        else:
            average.append(element)
    print('предприятия с прибылью ниже среднего: ', ', '.join([str(element.name) for element in less_average]))
    print('предприятия с прибылью выще среднего: ', ', '.join([str(element.name) for element in above_average]))


while i < amount_of_firms + 1:
    create_firm()
    i += 1

print(f'среднегодовая прибыль всех предприятий: {get_average_profit()}')

analyze()

