cont = 0
num = 0
flag = 0
while num != 999:
    num = int(input("insert any number, please:  to exit of program type 999 "))
    if num == 999:
        flag = num
    else:
        num = num
        sume = num + num
        cont += 1
print('end')
print('''
the total of number inserted was {}'''.format(cont))
print("total of number was {} ".format(sume))