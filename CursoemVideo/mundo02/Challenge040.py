#python 3.7.1

n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
avg = (n1+n2)/2

if avg <5:
  print('reprovado')
elif avg >=5 and avg< 7:
  print('recuperacao')
elif avg > 7.0:
  print('aprovado')    