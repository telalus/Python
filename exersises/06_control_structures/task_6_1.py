# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ipin = input('Enter your IP address: ')

ipaddress = ipin.split('.')

ip0 = int(ipaddress[0])
ip1 = int(ipaddress[1])
ip2 = int(ipaddress[2])
ip3 = int(ipaddress[3])

#ipaddress = [ip0,ip1,ip2,ip3]

if ip0 < 128:
  print('Class of inputed IP - A')
elif ip0 < 192:
  print('Class of inputed IP - B')
elif ip0 < 224:
  print('Class of inputed IP - C')
elif ip0 < 240:
  print('Class of inputed IP - D')
else:
  print('Class of inputed IP - E')

if ip0 == 0 and ip1 == 0 and ip2 == 0 and ip3 == 0:
  print('unassigned')
elif ip0 == 255 and ip1 == 255 and ip2 == 255 and ip3 == 255:
  print('local broadcast')
elif ip0 < 224:
  print('unicast')
elif ip0 < 240:
  print('multicast')
elif ip0 > 240:
  print('reserved')
else:
  print('unused')
