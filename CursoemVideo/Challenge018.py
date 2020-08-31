"""
Build an program that reads any angle
and shows on screen the value of your sine, cosine and tangent that angle
"""
import math
angle = float(input('Please little locust, insert any angle :  '))
print('The sine is ; {} \n'
      ' This cosine is {} \n'
      ' and Tangent is {}'.format(math.sin(angle), math.cos(angle), math.tan(angle)))
print('''
Remember that Sine is a result of opposite( another side of x or y) cathetus / hypotenuse 
Cosine adjacent cathetus / hypotenuse (beside of x or y) and tangent is opposite cathetus / adjacent cathetus ''')