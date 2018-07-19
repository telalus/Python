# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]

number = int(input('Enter number from list (2,7,10,11,15,30,50,100): '))
word = input('\nEnter word from list (python,ruby,perl): ')

num_reverse = num_list.copy()
num_reverse.reverse()
num = len(num_list) - (num_reverse.index(number) + 1)

word_reverse = word_list.copy()
word_reverse.reverse()
wrd = len(word_list) - (word_reverse.index(word) + 1)

print('\nПоследний раз ваше число встречается под индексом {}'.format(num))
print("\nПоследний раз ваше слово встречается под индексом {}".format(wrd))
