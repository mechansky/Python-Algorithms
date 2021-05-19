"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""



def func(n, number=1, result=0):
    print(result) if n == 0 else func(n-1, number, number + result / -2)


func(3)