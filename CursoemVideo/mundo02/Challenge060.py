from math import factorial
arg0 = int(input('insert an number to find its factorial N!'))
arg1 = factorial(arg0)
print('The factorial of {}! is {} x {} x {} ...x n = {}'.format(arg0, arg0-1, arg0-2, arg0-3, arg1))
