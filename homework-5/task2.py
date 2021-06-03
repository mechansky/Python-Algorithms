"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict

d = defaultdict(list)
first_number = input('введите первое шестнадцатиричное число: ')
second_number = input('введите второе шестнадцатиричное число: ')

d[first_number] = list(first_number)
d[second_number] = list(second_number)


result_sum = hex(int(first_number, 16) + int(second_number, 16))[2:].upper()
d[result_sum] = list(result_sum)

result_multiplication = hex(int(first_number, 16) * int(second_number, 16))[2:].upper()
d[result_multiplication] = list(result_multiplication)


print(f'Сумма чисел {d[first_number]} и {d[second_number]} = {d[result_sum]}')
print(f'Произведение чисел {d[first_number]} и {d[second_number]} = {d[result_multiplication]}')


class HexNumber:
    def __init__(self, number):
        self.number = int(number, 16)

    def __add__(self, other):
        result = self.number + other.number
        return f'{list(hex(result)[2:].upper())}'


    def __mul__(self, other):
        result = self.number * other.number
        return f'{list(hex(result)[2:].upper())}'



number_1 = HexNumber('A2')
number_2 = HexNumber('C4F')

number_3 = number_1 + number_2
number_4 = number_1 * number_2

print(f'результат сложения: {number_3}')
print(f'результат умножения: {number_4}')
