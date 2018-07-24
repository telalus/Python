# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_template = '''
Protocol:           OSPF
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}
'''
with open('ospf.txt', 'r') as oft:
  for line in oft:
    ospf = line.replace('[', '').replace(']', '').replace(',', '')
    ospfs = ospf.split()
    print(ospf_template.format(ospfs[1], ospfs[2], ospfs[4], ospfs[5], ospfs[6]))
