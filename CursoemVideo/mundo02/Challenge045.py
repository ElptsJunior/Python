#Joquenpo
print ("""1 Pedra
2 papel 
3 tesoura""")

import random
selected = str(input(' escolha seu numero'))
print('Jo')
print("ken")
print("po")
opcoes = random.randint(1,3)
if selected == 1 and opcoes == 1:
    print("empate")
elif selected == 1 and opcoes == 2:
        print("Pedra perde pro papel")
elif selected == 1 and opcoes == 3:
    print(" pedra ganha da tesoura")









"""if  selected == "stone" and   cpu == "paper":
  print("you choose {} and cpu choose {}".format(selected, cpu))
elif selected in ('scisor') and cpu in ('paper'):
  print("you choose {} and cpu choose {}".format(selected, cpu))
"""