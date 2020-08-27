'''Build in an program that read's an float number and show's your integer part  for exemple insirted 6.1234
the result is 6
'''
from math import trunc    #This module brings the function truncate from bibliotec math
print('='*200)
number = float(input('Please little Locust insert any number please  : '))
print('='*200)
print('The number {} has the full part is {} '.format(number, trunc(number)))