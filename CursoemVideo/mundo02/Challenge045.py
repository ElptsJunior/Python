#Joquenpo
from time import sleep # sera usado para dar aquele intervalo entre os prints
from random import randint
print ("""0 Pedra
1 papel 
2 tesoura""")
capa = ('Pedra','Papel', 'Tesoura')

player = int(input(' escolha seu numero'))
cpu = randint(0,2)# Sorteia numeros entre 0,1,2
resul = player,cpu
print('Jo')
sleep(1)
print("ken")
sleep(1)
print("po")

print(" A maquina escolheu {}".format(capa[cpu]))# mascara os valores de capa sobre os numeros de cpu dentro na posicao
print(" o jogador jogou {}".format(capa[player]))
# Possibilidades da
# Tesoura
if resul == (2,0):
    print("Tesoura perde pra pedra ")

elif resul == (2,1):
    print("Tesoura vence o papel")
elif resul == (2,2):
    print("Empate")

# Possibilidades do papel
if resul == (1,0):
    print("Papel vence pedra")

elif resul == (1,1):
    print("Empate")
elif resul == (1,2):
    print("Papel perde para tesoura")

# Possibilidades da Pedra
if resul == (0,0):
    print("empate")

elif resul == (0,1):
    print("Pedra perde pro papel")
elif resul == (0,2):
    print("Pedra vence a tesoura")


