#Challenge041
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento?'))
idade = atual - nasc

if idade <= 9:
  print(' voce tem {} anos, pertente a categoria Mirim'.format(idade))
elif  idade >=10 and idade < 14:
  print(' voce tem {} anos pertence a categoria Infantil'.format(idade))
elif idade>=15 and idade <=19:
  print('voce tem {}anos pertence a categoria junior'.format(idade))
elif idade  == 20:
   print('voce tem {}anos sua categoria e a de senior'.format(idade))
else:
   print('voce pertence a categoria master')

