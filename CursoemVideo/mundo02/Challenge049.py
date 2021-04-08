from time import sleep
print('='*32)
print('\033[07m Multiplication table: \033[m')
print('='*32)
choice = int (input('insert a number for multiplication table'))
for index in range(0,11): # for corre de 0 a 10
    resul = choice * index
    print('\033[032m {}\033[m x {} = \033[04m {} \033[m'.format(choice,index,resul))
    sleep(1)