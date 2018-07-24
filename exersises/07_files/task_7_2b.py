# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
with open('config_sw1.txt', 'r') as config:
  for line in config:
    out = open('config_sw1_cleared.txt', 'a')
    if line.find(ignore[0]) != -1 or line.find(ignore[1]) != -1 or line.find(ignore[2]) != -1:
      pass
    else:
      out.write(line)
      out.close()
