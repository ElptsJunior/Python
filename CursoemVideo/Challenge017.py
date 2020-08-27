'''
Challenge 017:
Build an program that's read the length of opposite Cathetus and adjacent of triangle retangle, calc the
hypothenuse.
https://pt.wikihow.com/Encontrar-o-Comprimento-da-Hipotenusa
a² + b² = c²
'''
import math
print('='*200)
a = int(input('Welcome Little Locust!, Please insert the value of first cathetus a²:  '))# type: int
print('Ok, a² = {}² is equal the {}'.format(a, pow(a, 2)))
b = int(input('Ok , Now  we need of the second cathetus like b²:  '))
print('All right ! , The opposite cathetus b² = {}² and the result is {}'.format(b, pow(b, 2)))
c = int(math.sqrt(math.pow(a, 2)+ math.pow(b, 2))) # Or  c = square root ( result / 0.5) result is a** + b**
print('='*200)
print('''Now , we have the all values to arrive the hypotenuse. but let's check and explain step by step
The value of C² Hypotenuse {2}
it's the summation of a² = {0} + b² = {1} as a result c²{2} 
But to reach the length of triangle we need to find the raw value using the square root Number / 0.5
in this case {2}/0.5 or (1/2) , because the result of c was powered of two ,
thus the Square root of Hypotenuse is {5}
is the same thing of length of opposite cathetus!
'''.format(pow(a, 2), pow(b, 2),  (pow(a, 2)+pow(b, 2)), a, b, math.sqrt(pow(a, 2)+ pow(b, 2))))

