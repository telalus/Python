# -*- coding: utf-8 -*-
'''
Задание 6.2

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX.
Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.

Создать скрипт, который преобразует MAC-адреса в формат cisco
и добавляет их в новый список mac_cisco

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []

for mc in mac:
  num = mac.index(mc)
  mc = mc.replace(':','.')
  mac_cisco.insert(num, mc)

else:
  print('Исходный список МАС:\n')
  print(mac)
  print('\nСписок МАС в формате cisco:\n')
  print(mac_cisco)
