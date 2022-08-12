# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 00:11:32 2022

@author: csimo
"""


def mystery(values):
    
     count = 0
     for i in range(len(values)):
         print('i value[i] and value[i-1]',i,values[i],values[i-1])
         if values[i] > values[i-1]:
             count += 1
             print('count',count)
     return count



#print(mystery([8, 5, 3, 7, 1, 6]))



for x in [2, 4, 6]:
    print('x',x)
    for y in range(1, x):
        print('range', range(1,x))
        print('y', y)
        print('x+y',x + y)
# print('print x, y', x, y)

a = 12
b = 4
print('a,b', a, b)

while a > 2:
    print('a, b', a, b)
    a -= b
    b -= 1
    print(a, b)