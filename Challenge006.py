print('='*130)
print(' \033[7m  Build an program that read a number and shows the double, triple and square root : \033[m ' )
print('='*130)

from math import sqrt
number = int(input(' type an number:'))
double = number.__pow__(2)
triple = number.__pow__(3)
squareroot = sqrt(number)
print('''The double of {} is {} \n
 and the Triple of {} is {} \n
 and finally the square root of {} is {} but if you wish to read in less digit's {:.2f}'''.capitalize()
      .format(number, double, number, triple, number, squareroot,squareroot))