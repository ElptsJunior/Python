from time import sleep
menu = 0
while menu != 5:
    a = int(input("insert the first number: "))
    b = int(input('insert the second number: '))
    sleep(1)
    print('right!')
    sleep(2)
    print('Now pick one of operation botton:')
    sleep(1)
    menu = int(input('''
    [1] for sum
    [2] for multiplicate
    [3] for max
    [4] for enter new numbers
    [5] for exit of program   
    
    '''))

    if menu == 1:
       print( 'the summation of {} + {} was {}'.format(a,b,(a+b)))
    elif menu == 2:
        print('the multplication of {} * {} was '.format(a,b,(a*b)))
    elif menu == 3:
        if a > b:
            wopper = a
        else:
            wopper = b
        print('the max value insert between {} & {} was :'.format(a,b,wopper))
    elif menu == 4:

        a = int(input("insert the first number: "))
        b = int(input('insert the second number: '))
        sleep(1)
        print('right!')
        sleep(2)
        print('Now pick one of operation botton:')
        sleep(1)
        menu = int(input('''
        [1] for sum
        [2] for multiplicate
        [3] for max
        [4] for enter new numbers
        [5] for exit of program '''))
    else:
        print('incorrect option')
        sleep(3)
        print('reloading')
        sleep(1)
        print(".")
        sleep(1)
        print('..')
        sleep(2)
        print('...')
print('Come back soon little locust!')