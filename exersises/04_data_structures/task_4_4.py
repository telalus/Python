# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

In : com1 = command1.split()

In : com2 = command2.split()

In : com1
Out[61]: ['switchport', 'trunk', 'allowed', 'vlan', '1,3,10,20,30,100']

In : com2
Out[61]: ['switchport', 'trunk', 'allowed', 'vlan', '1,3,100,200,300']

In : com1 = com1[4].split(',')

In : com2 = com2[4].split(',')

In : com1
Out: ['1', '3', '10', '20', '30', '100']

In : com2
Out: ['1', '3', '100', '200', '300']

In : com1 = [int(vlan) for vlan in com1]

In : com2 = [int(vlan) for vlan in com2]

In : com1
Out: [1, 3, 10, 20, 30, 100]

In : com2
Out: [1, 3, 100, 200, 300]

In : command = list((set(com1))&(set(com2)))

In : command
Out: [1, 3, 100]
