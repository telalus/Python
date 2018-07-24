# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlanlist = []
with open('CAM_table.txt', 'r') as mactable:
  for line in mactable:
    if line.find('DYNAMIC') != -1:
      sline = line.replace('  DYNAMIC  ', '')
      vlanlist.append(sline.strip())
    else:
      pass
vlanlist.sort()
for vlanline in vlanlist:
  print (vlanline)
