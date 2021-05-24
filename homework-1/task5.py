"""
Задание 5.
Задание на закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

class Table():
    def __init__(self, *args):
        self.elems = []

    def create_stack(self, *args):
        self.plates = []

    def put_in_stack(self, element):
        return self.plates.append(int(element))

    def amount_of_plates(self):
        return sum(self.plates)

    def create_new_stack(self, *args):
        leftovers = sum(self.plates) - 10
        self.plates.insert(0, 10 - sum(self.plates[:-1]))
        self.plates.pop()
        self.elems.append(self.plates)
        while leftovers >= 10:
            self.elems.append(10)
            leftovers = leftovers - 10
        print(f'стопка заполнена! всего стопок: {len(self.elems)}, в следующую стопку/ки пойдет тарелок: {leftovers} шт!')
        self.plates.clear()
        if leftovers < 10:
            self.plates.insert(0, leftovers)  # 1 способ реализации

        # 2 способ реализации
        # self.leftovers = sum(self.plates) - 10
        # self.elems.append(sum(self.plates) - self.leftovers)
        # while self.leftovers >= 10:
        #     self.elems.append(10)
        #     self.leftovers = self.leftovers - 10
        # print(f'стопка заполнена! всего стопок: {len(self.elems)}, в следующую стопку/ки пойдет тарелок: {self.leftovers} шт!')
        # self.plates.clear()
        # self.plates.append(self.leftovers)


    def show_table(self, *args):
        print(f'всего на столе стопок: {len(self.elems)}')


table1 = Table()


def plate_in_a_stack():
    table1.create_stack()
    while True:
        number = input('введите количество тарелок, которые пойдут в стопку (для выхода введите "q"): ')
        if number == 'q':
            table1.show_table()
            break
        table1.put_in_stack(number)
        if table1.amount_of_plates() > 10:
            table1.create_new_stack()


plate_in_a_stack()
