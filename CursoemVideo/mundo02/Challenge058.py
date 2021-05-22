from random import randint
from time import sleep
ntimes = 1
cpu = randint(0,10)
player = int(input('guess what number between zero until 10 was choosen:  '))
while player != cpu:
    print('Nop!, try again')
    if player < cpu:
        print(' tip ! more..')
    else:
        print(' tip less..')
    ntimes += 1
    player = int(input('Guess again what number was choosen by me kk'))
print('Congratulation !!!!')
sleep(1)
print('bullseyes .')
sleep(2)
print('the number choose by me was {}'.format(cpu))
sleep(3)
print('and you tried {} times'.format(ntimes))