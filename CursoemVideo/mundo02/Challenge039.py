# Desafio 039:

# Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com sua
#  idade:

# _ Se ele ainda via se alistar ao serviço
# militar.

# - Se é a hora de se alistar.

# - Se já  passou do tempo do alistamento.

# Seu programa também deve mostrar o tempo
# que falta ou que passou do prazo.
from datetime import date

atual = date.today().year
nasc = int(input("digite seu ano de nasc"))
idade = atual - nasc

if idade == 18:
    print('voce tem 18 anos e hora de se alistar')
elif idade > 18:
    dif = 18 - idade
    print("voce tem {} anos ! ja se apresentou a {} anos atras".format(idade, dif))
elif idade > 18:
    dif = idade - 18
