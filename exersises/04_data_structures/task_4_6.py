# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf = ospf_route.replace('[', '').replace(']', '').replace(',', '')
ospf = ospf.split()
ospf.pop(0)
ospf.pop(2)
ospf.insert(0, 'OSPF' )
ospf_test = dict([('Protocol', ospf[0]), ('Prefix', ospf[1]), ('AD/Metric', ospf[2]), ('Next-Hop', ospf[3]), ('Last update', ospf[4]), ('Outbound Interface', ospf[5])])
ospf_test
