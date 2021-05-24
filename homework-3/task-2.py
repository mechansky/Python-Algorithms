from uuid import uuid4
import hashlib

salt = uuid4().hex
passwd = input('введите пароль: ')
hsh = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
print(f'В базе данных хранится строка {hsh}')

f = open('passw.txt', 'w')
f.write(hsh)
f.close()

user_answer = input('введите пароль для проверки: ')
f = open('passw.txt', 'r')
if hashlib.sha256(salt.encode() + user_answer.encode()).hexdigest() == f.read():
    print('вы ввели верный пароль')
else:
    print('пароль неправильный')
f.close()
