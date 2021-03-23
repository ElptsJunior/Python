#Challenge042


v1 = float(input(' medida 1: '))
v2 = float(input(' medida 2: '))
v3 = float(input(' medida 3: '))
#if v1+v2+v3 == 180:
if v1 == v2 == v3:
   print('Triangulo equilatero: com todos os lados iguais')
elif (v1 == v2 or v3) and (v2 == v1 or v3 ):
   print('tringulo isoceles dois lados iguais')
elif (v1 != v2 or v3) and (v2 != v1 or v3) and (v3 != v1 or v2):
  print('escaleno')
else:
  print('nao e um triangulo')    