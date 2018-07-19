# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ipin = input('Enter your IP address: ')

if ipin.count('.') == 3:
  ipaddress = ipin.split('.')
  ip0 = int(ipaddress[0])
  ip1 = int(ipaddress[1])
  ip2 = int(ipaddress[2])
  ip3 = int(ipaddress[3])
  if 0 <= ip0 <= 255 and 0 <= ip1 <= 255 and 0 <= ip2 <= 255 and 0 <= ip3 <= 255:
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
  else:
    print('Incorrect IPv4 address')
else:
  print('Incorrect IPv4 address')
