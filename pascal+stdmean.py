# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:30:16 2018

@author: Hanna
"""
from math import factorial, sqrt
from time import sleep
'rad i, kolumn j'

'''Det här är lab2, med del A: pascals triangel och del B: medelvärde och standardavvikelse'''


def user_choice():
    '''
    Press P for Pascals triangle and M for standard deviation and mean
    '''
    x = True
    while x==True:
        user_input = input('Tryck P för Pascals triangel eller M för medelvärde och standardavvikelse: ')
        if user_input == 'P' or user_input == 'M':
            x=False
            return user_input
        else:
            print('Try again!')

def rows():
    '''
    Enter a positive integer
    '''
    y = True
    while y==True:
        user_num = input('Hur många rader av Pascals triangel vill du skriva ut? ')
        try:
            number = int(user_num)
            if number > 0:
                y = False
                return number
            else:
                print('Not a positivte number, try again!')
        except:
            print('Not a number, try again!')
            
def pascals_triangel(n):
    '''
    takes user input number of rows and prints pascals triangel in a dramatic, slow way.
    '''
    for i in range(0, n):
        rad = ''
        for j in range(0, i+1):
            number = str(binom(i,j))
            rad += number + ' '
        print (rad)
        sleep(1)
    if n > 2:
        print('Math is truly beautiful!')

def binom(i, j):
    '''
    calculates the binominal factor for row i and column j
    '''
    number = int(factorial(i)/(factorial(j) * (factorial(i-j))))
    return number

      
def mean_standard(file):
    '''
    enter a file name with one number per line, the program returns mean and standard deviation
    '''
    A = 0
    B = 0
    n = 0
    text = open(file, 'r')
    for line in text:
        n += 1
        number = float(line)
        A += number
        B += number**2
    if n > 0:
        mu = A/n
        sigma = sqrt((B + n*mu**2 - 2*mu*A) / (n - 1))
        print (u'\u03BC' + '=' + str(mu))
        print(u'\u03C3' + '=' + str(sigma))
    else:
        print('Din fil var tom :(')

def main():
    '''
    the mainframe of the program
    '''
    print('''Det här programet låter dig skriva ut n rader av pascals triangel \neller beräkna medelvärde och standardavvikelse av siffror i en textfil''')
    choice = user_choice()
    if choice == 'P':
        n = rows()
        print('Calculating...')
        sleep(1)
        pascals_triangel(n)
    elif choice == 'M':
        file = input('Vad är namnet på din fil? ')
        mean_standard(file)
main()