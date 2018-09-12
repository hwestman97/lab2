# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:30:16 2018
@author: Hanna
"""
from math import factorial, sqrt
from time import sleep

'''Det här är lab2, med del A: pascals triangel och del B: medelvärde och standardavvikelse'''


def user_choice():
    '''
    Frågar användaren om datorn ska köra Pascals triangel eller beräkna standardavvikelse/medelvärde
    '''
    x = True
    while x==True:
        user_input = input('Tryck P för Pascals triangel eller M för medelvärde och standardavvikelse: ')
        if user_input == 'P' or user_input == 'M':
            x = False
            return user_input
        else:
            print('Försök igen!')

def rows():
    '''
    Hämtar indata från användaren och testar om det faktiskt är ett positivt heltal
    Använder sig av try/except för att testa om indatan är ett heltal
    '''
    y = True
    while y==True:
        user_num = input('Hur många rader av Pascals triangel vill du skriva ut? ')
        try:
            number = int(user_num)
            if number > 0 and number < 20:
                y = False
                return number
            elif number <= 0:
                print('Inte ett positivt heltal, försök igen!')
            else:
                print('Orkar inte, gör det själv')
        except:
            print('Inte ett heltal, försök igen!')
            
def pascals_triangel(n):
    '''
    Tar indata antal rader av Pascals triangel och skriver ut dem på ett långsamt och dramatiskt vis.
    '''
    for i in range(0, n):
        rad = ''
        for j in range(0, i+1):
            number = str(binom(i,j))
            rad += number  + ' '
        print (rad)
        sleep(1)
    if n > 2:
        print('Matematik är verkligen vackert!')

def binom(i, j):
    '''
    beräknar binominalfaktorn för rad i och kolumn j
    '''
    number = int(factorial(i)/(factorial(j) * (factorial(i-j))))
    return number

      
def mean_standard(file):
    '''
    skriv in filnamnet, funktionen beräknar standardavvikelse och medelvärde
    '''
    A = 0
    B = 0
    n = 0
    #with open() as f:
    text = open(file, 'r')
    for line in text:
        n += 1
        number = float(line)
        A += number
        B += number**2
    if n > 0:
        mu = A/n
        sigma = sqrt((B + n*mu**2 - 2*mu*A) / (n - 1))
        print('Medelvärdet är ' + u'\u03BC' + ' = ' + str(mu))
        print('Standardavvikelsen är ' + u'\u03C3' + ' = ' + str(sigma))
    else:
        print('Din fil var tom :(')

def main():
    '''
    programmets mainframe
    '''
    print('''Det här programet låter dig skriva ut n rader av pascals triangel \neller beräkna medelvärde och standardavvikelse av siffror i en textfil''')
    choice = user_choice()
    if choice == 'P':
        n = rows()
        print('Beräknar...')
        sleep(1)
        pascals_triangel(n)
    elif choice == 'M':
        file = input('Vad är namnet på din fil? ')
        mean_standard(file)

main()