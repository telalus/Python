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

In : ospf = ospf_route.replace('[', '').replace(']', '').replace(',', '')

In : ospf = ospf.split()

In : ospf
Out: ['O', '10.0.24.0/24', '110/41', 'via', '10.0.13.3', '3d18h', 'FastEthernet0/0']

In : ospf.pop(0)
Out: 'O'

In : ospf
Out: ['10.0.24.0/24', '110/41', 'via', '10.0.13.3', '3d18h', 'FastEthernet0/0']

In : ospf.pop(2)
Out: 'via'

In : ospf
Out: ['10.0.24.0/24', '110/41', '10.0.13.3', '3d18h', 'FastEthernet0/0']

In : ospf.insert(0, 'OSPF' )

In : ospf
Out: ['OSPF', '10.0.24.0/24', '110/41', '10.0.13.3', '3d18h', 'FastEthernet0/0']

In : ospf_test = dict([('Protocol', ospf[0]), ('Prefix', ospf[1]), ('AD/Metric', ospf[2]), ('Next-Hop', ospf[3]), ('Last update', ospf[4]), ('Outbound Interface', ospf[5])])

In : ospf_test
Out:
{'Protocol': 'OSPF',
 'Prefix': '10.0.24.0/24',
 'AD/Metric': '110/41',
 'Next-Hop': '10.0.13.3',
 'Last update': '3d18h',
 'Outbound Interface': 'FastEthernet0/0'}

