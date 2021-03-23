#Challenge043

peso = float(input("seu peso é? :"))
alt = float(input ("sua altura é "))
imc = peso / alt
print(imc)

if imc < 18.5:
  print("você esta abaixo so peso")
elif imc == 18.5 and  imc <=25 :
  print("você esta em seu peso ideal")
elif imc == 26 and  imc <= 30 :
  print("sobrepeso ")
elif imc  == 31 and imc <=40 :
  print("obesidade ")
else:
  print("obesidade mórbida")  