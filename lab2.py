# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:30:16 2018

@author: Hanna
"""
from math import factorial
'rad i, kolumn j'
'''Det här är lab2, med pascals triangel och '''

def pascals_triangel(n):
    for i in range(0, 4):
        for j in range(0, i+1):
            number = binom(i,j)
            print(number)
        print ('''\n''')

def binom(i, j):
    number = factorial(i)/(factorial(j) * (factorial(i-j)))
    return number
      
def start():
    print('''Det här programet låter dig skriva ut n rader av pascals triangel 
          eller nån annan skit''')
    user_choice = input('Tryck P för Pascals triangel eller S för skit: ')
    if user_choice == 'P':
        n = input('Hur många rader av Pascals triangel vill du skriva ut? ')
        pascals_triangel(n)
        
start()

    