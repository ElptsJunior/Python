# Crie uma frase qualquer e diga se essa frase é um palindromo( que da per ler de trás pra frente e vice e versa)
from random import randint
frase = str(input('digite uma frase palindromo: '))
print(frase)
print(frase[::-1])
if frase == frase[:: -1]:
    print('A frase acima fica igual de tras pra frente , logo e um palindromo')
else:
    print('as frases acima sao diferentes')


