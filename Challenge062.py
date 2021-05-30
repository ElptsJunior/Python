index = 1
loop = 10
term = int(input('insert the 1first term: '))
while term != 0:
   #term = int(input('insert the 1first term: '))
    reason =int (input('insert the interval of P.a :'))
    pa = term
    while index <= loop:
        print('{}->'.format(pa), end='')
        pa += reason
        index += 1
    loop = int(input('how many time do you whant to repeat?: '))
    for index in range(index, loop):
        print("{}->".format(pa), end='')
        pa += reason
        index += 1
    term = int(input('insert the 1first term again: '))
    index = 0


