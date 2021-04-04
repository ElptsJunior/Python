#Contagem regressiva
# importando o modulo sleep de time
from time import sleep
from datetime import date


for contador in range(10,0,-1):
    print(contador)
    sleep(1)
print("Feliz {}".format(date.year.))