print('='*100)
print('build an program that read of 0 until 9999 and separe each one , by dozen, hundred e Thousand')
print('='*100)
number = int(input('Please type any number '))
#Using math rules for slash the number as string
un = number // 1 % 10
do = number // 10 % 10
hu = number // 100 % 10
th = number // 1000 % 10

print('Unit of This number is : {}'.format(un))
print('Dozen of This number {}'.format(do))
print('Hundred of This number {}'.format(hu))
print("Thousand of this number {}".format(th))