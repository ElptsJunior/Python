#Desafio 038:

#Escreva um programa que leia dois valores numéricos inteiros e compare- os, mostrando na tela uma mensagem:

#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe maior, os dois são iguais

v1 = int(input("digite o primeiro valor"))
v2 = int(input("digite o segundo valor"))
if v1 > v2:
  print('v1 e maior que v2')
elif v1 < v2:
  print('v1 menor que v2')
else:
  print('valores com mesmo valor')
