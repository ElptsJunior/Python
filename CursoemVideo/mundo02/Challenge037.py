# Desafio 037:
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão :
# _ 1 para binário
# _ 2 para octál
# _ 3 para hexadecimal

num = int(input('escreva um número inteiro:  '))

print('digite:')
print("1 para binário")
print("2 para octál")
print("3 para hexadecimal")

opcao = int(input("sua escolha uma de suas bases de conersao :"))

if opcao == 1:
    print("o valor digitado {} em binario fica assim {}".format(num, bin(num[2:])))
    # o fatiamento de string udado para ocultar as dus primeiras casas 0b
elif opcao == 2:
    print(" o valor digitado {} em octál fica assim {}".format(num, oct(num[2:])))
elif opcao == 3:
    print("o valor digitado {} em hexadecimal fica assim {}".format(num, hex(num[2:])))
else:
    print("Opcao invalida ")

