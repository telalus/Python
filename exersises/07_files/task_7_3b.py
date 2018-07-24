# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlanlist = []
vlannum = input('Enter VLAN number: ')
with open('CAM_table.txt', 'r') as mactable:
  for line in mactable:
    if line.find('DYNAMIC') != -1:
      sline = line.replace('  DYNAMIC  ', '')
      vlanlist.append(sline.strip())
    else:
      pass
for vlanline in vlanlist:
  if vlanline.startswith(vlannum):
    print (vlanline)
  else:
    pass
