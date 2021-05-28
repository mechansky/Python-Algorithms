"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    enter_num = (list(str(enter_num)))
    enter_num.reverse()
    enter_num = ''.join(map(str,enter_num))
    return enter_num

print(revers_4(20050))

print(f'reverse_1 time: ',
    timeit(
        "revers_1(20050)",
        globals=globals(),
        number=100000
    ))


print(f'reverse_2 time: ',
    timeit(
        "revers_2(20050)",
        globals=globals(),
        number=100000
    ))


print(f'reverse_3 time: ',
    timeit(
        "revers_3(20050)",
        globals=globals(),
        number=100000
    ))

print(f'reverse_4 time: ',
    timeit(
        "revers_4(20050)",
        globals=globals(),
        number=100000
    ))

def main():
    revers_1(20050)
    revers_2(20050)
    revers_3(20050)
    revers_4(20050)

run('main()')

# как показывает анализ, revers_3 работает быстрее всего, поскольку использует встроенную функцию (используя срез)
# revers_4 - самая долгая функция, так как использует формирование списка, после чего переворот списка через reverse
# и объединение позиций списка - это самая долгая процедура - слишком много действий
