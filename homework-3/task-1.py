import time


def list_input(lst, elements):
    for element in range(1, elements):
        lst.append(element) # O(1)


start = time.time()
lst = []
list_input(lst, 1000000) # O(1)
lst.append(123) # O(1)
lst.pop()  # O(1)
len(lst)  # O(N)
min(lst) # O(N)
lst.extend('asd')  # O(3)
end = time.time()
print(f'на выполнение методов со списками затратилось {end - start} с.')

# сложность - O(N)


def dict_input(d, elements):
    for element in range(1, elements):
        d[element] = element  # O(1)

start = time.time()
d1 = {}
dict_input(d1, 1000000)
d1.keys()  # O(1)
d1.popitem()  # O(1)
d1['new_key'] = 'new_value'  # O(1)
end = time.time()
print(f'на выполнение методов со словарями затратилось {end - start} с.')

# сложность - O(1)

#в целом, и по О(нотации) и по времени, меньше времени затрачивают операции со словарями, т.к. бОльшая часть операций
#со словарями являются константами, в то время, как у списков они зависят от количества добавляемых элементов (extend)
#вычисления min/max значения