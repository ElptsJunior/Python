#Contagem regressiva
# importando o modulo sleep de time
from datetime import date
from time import sleep

for contador in range(10,0,-1): # conta de 10 a 0 de -1 e de decresente
    print(contador)
    sleep(1)
print("Fireworks ")
sleep(3)
print(" Happy new year  {}".format(date.today().year)) #traz ao usuario a informacao do ano atual