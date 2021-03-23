#Joquenpo

import random
selected = str(input('pick an stone, paper or scisor'))
cpu = random.choice("paper, scisor")

if  selected == "stone" and   cpu == "paper":
  print("you choose {} and cpu choose {}".format(selected, cpu))
elif selected in ('scisor') and cpu in ('paper'):
  print("you choose {} and cpu choose {}".format(selected, cpu))
