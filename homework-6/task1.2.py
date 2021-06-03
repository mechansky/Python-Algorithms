from numpy import array
import random
from pympler import asizeof
from memory_profiler import profile

@profile
def func_1():
    profits_per_day = []
    total = 0
    for element in range(1024):
        profits_per_day.append(random.randint(-100000, 1000000))
    for element in profits_per_day:
        total += element
    print(f'всего заработано {total} рублей')
    print(f'размер списка с прибылями: {asizeof.asizeof(profits_per_day)}')


@profile
def func_2():
    profits_per_day = array([random.randint(-100000, 1000000) for element in range(1024)])
    total = sum(profits_per_day)
    print(f'всего заработано {total} рублей')
    print(f'размер списка с прибылями: {asizeof.asizeof(profits_per_day)}')

func_1()
func_2()

# здесь, несмотря на то, что памяти расходуется одинаково в обоих вариантах, с помощью NumPy мы сократили в 5 раз
# вес списка, где хранится прибыль за каждый день (условно)
