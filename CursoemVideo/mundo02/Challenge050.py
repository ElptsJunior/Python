masc =('Primeiro', 'Segundo','Terceiro','Quarto','Quinto','Sexto')
s = 0
cont = 0
for index in range(0,6):
    num = int(input('Digite o \033[07m{}\033[m numero'.format(masc[index])))
    if num % 2 == 0:
        s += num
        print(s)