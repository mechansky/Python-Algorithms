"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

def reverse_number(number, rev_number=0):
    if number == 0:
        print(rev_number)
        return number
    rev_number = rev_number * 10 + (number % 10)
    reverse_number(number // 10, rev_number)


reverse_number(34860)