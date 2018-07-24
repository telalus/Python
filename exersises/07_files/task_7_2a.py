# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt', 'r') as config:
  for line in config:
    if line.startswith('!') or line.find(ignore[0]) != -1 or line.find(ignore[1]) != -1 or line.find(ignore[2]) != -1:
      pass
    else:
      print(line.rstrip())
