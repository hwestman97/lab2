# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:30:16 2018

@author: Hanna
"""
from math import factorial, sqrt
'rad i, kolumn j'
'''Det här är lab2, med del A: pascals triangel och del B: medelvärde och standardavvikelse'''

def pascals_triangel(n):
    for i in range(0, n):
        rad = ''
        for j in range(0, i+1):
            number = str(binom(i,j))
            rad += number + ' '
        print (rad + '''\n''')

def binom(i, j):
    number = int(factorial(i)/(factorial(j) * (factorial(i-j))))
    return number
      
def mean_standard(file):
    A = 0
    B = 0
    text = open(file, 'r')
    n = 0
    for line in text:
        n += 1
        number = int(line)
        A += number
        B += number**2
    mu = A/n
    sigma = sqrt((B + n*mu**2 - 2*mu*A) / (n - 1))
    print (u'\u03BC' + '=' + str(mu))
    print(u'\u03C3' + '=' + str(sigma))

def start():
    print('''Det här programet låter dig skriva ut n rader av pascals triangel \neller beräkna medelvärde och standardavvikelse av siffror i en textfil''')
    user_choice = input('Tryck P för Pascals triangel eller M för medelvärde och standardavvikelse: ')
    if user_choice == 'P':
        n = int(input('Hur många rader av Pascals triangel vill du skriva ut? '))
        pascals_triangel(n)
    elif user_choice == 'M':
        file = input('Vad är namnet på din fil? ')
        mean_standard(file)
start()


    