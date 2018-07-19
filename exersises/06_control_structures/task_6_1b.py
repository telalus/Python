# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ipin = input('Enter your IP address: ')
 
while True:
  if ipin.count('.') != 3:
    print('\nIncorrect IPv4 address')
  else:    
    ipaddress = ipin.split('.')
    ip0 = int(ipaddress[0])  
    ip1 = int(ipaddress[1])
    ip2 = int(ipaddress[2]) 
    ip3 = int(ipaddress[3])    
    if ip0 > 255 or ip1 > 255 or ip2 > 255 or ip3 > 255:
      print('\nIncorrect IPv4 address')
    elif ip0 < 0 or ip1 < 0 or ip2 < 0 or ip3 < 0:
      print('\nIncorrect IPv4 address')
    else:  
      if ip0 < 128:      
        print('Class of inputed IP - A') 
      elif ip0 < 192:      
        print('Class of inputed IP - B')
      elif ip0 < 224:      
        print('Class of inputed IP - C') 
      elif ip0 < 240:      
        print('Class of inputed IP - D')
      else:      
        print('Class of inputed IP - E') 
      if ip0 == 0 and ip1 == 0 and ip2 == 0 and ip3 == 0:      
        print('unassigned')    
      elif ip0 == 255 and ip1 == 255 and ip2 == 255 and ip3 == 255:  
        print('local broadcast')    
      elif ip0 < 224:      
        print('unicast')    
      elif ip0 < 240:      
        print('multicast')    
      elif ip0 > 240:      
        print('reserved')    
      else:      
        print('unused')  
      break 
  ipin = input('\nEnter your IP address again: ')
