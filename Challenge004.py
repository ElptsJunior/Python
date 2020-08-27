print('='*100)
print('''BUILD AN SCRIPT THAT CHECK PRIMITIVE TYPE AND RETURN TO USER'''.title())
print('='*100)

value = input('Please insert any value : \n')
print('primary type {}'.format(type(value)))
print('any spaces ?: {}'.format(value.isspace()))
print('Is numeric ?: {}'.format(value.isnumeric()))
print(' is alphanumeric {}'.format(value.isalnum()))
print('is an upper case {}'.format(value.isupper()))

