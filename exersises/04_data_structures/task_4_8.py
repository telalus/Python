# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1'
ip = IP.split('.')
ip0=int(ip[0])
ip1=int(ip[1])
ip2=int(ip[2])
ip3=int(ip[3])
ip_template = '''
{:10} {:10} {:10} {:10}
{:10b} {:10b} {:10b} {:10b}
'''
print(ip_template.format(i1, i2, i3, i4, i1, i2, i3, i4))
