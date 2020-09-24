
number = int(input('\033[7m Welcome little locust! , please insert any number \033[m \n' ))

double = pow(number, 2)
triple = pow(number, 3)
square_root = pow(number, 0.5) # Or if you want calc by precedence order , type number**0.5 or mumber**(1/2)
print('let me see... \n this number{0} powered to the two is {1}\n the Triple is {2} and the Square Root is : {3}'
      .format(number, double, triple, square_root))
print('='*200)
print('Or The Square root in contract mode is {:2.3f} '.format(square_root))
