print('='* 200)
print('Build an program that read the name inserted and check if have silva ')
print('='* 200)
name = str(input('Please insert your full name:').lower()).strip()
check = ('silva')in name
print(check)