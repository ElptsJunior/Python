#Joquenpo
from random import randint
print ("""1 Pedra
2 papel 
3 tesoura""")

player = int(input(' escolha seu numero'))
cpu = randint(1,3)# sorteia de 1 a 3
resul = player,cpu
print('Jo')
print("ken")
print("po")

print(" A maquina escolheu {}".format(cpu))
# Possibilidades da
# Tesoura
if resul == (3,1):
    print("Tesoura perde pra pedra ")

elif resul == (3,2):
    print("Tesoura vence o papel")
elif resul == (3,3):
    print("Empate")

# Possibilidades do papel
if resul == (2,1):
    print("Papel vence pedra")
    print("jogador vence")
elif resul == (2,2):
    print("Empate")
elif resul == (2,3):
    print("Papel perde para tesoura")

# Possibilidades da Pedra
if resul == (1,1):
    print("empate")

elif resul == (1,2):
    print("Pedra perde pro papel")
elif resul == (1,3):
    print("Pedra vence a tesoura")


