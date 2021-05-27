index = 1
firstterm = int(input('Insert the first term'))
reason = int(input('insert the interval of aritmetical progresom '))
term = firstterm
while index <= 10:
    index += 1
    term += reason
    print('{} ->'.format(term),end= '')# tirar o final da linha assim o resultado vai pro lado
