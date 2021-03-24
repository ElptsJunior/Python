"""Elabore um progra,a que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao
de pagamento
"""
price = float(input("qual o valor do produto ?"))
print('''
Formas de pagamento :

- `a vista dinheiro / cheque :
10 % de desconto
- a vista rotativo : 5% dde desconto
- em ate 2x no cartao: preco normal

- em 3 vezes ou mais no cartao : 20 % de juros 

sendo assim: escolha

- 1 a vista
- 2 rotativo
- 3  parcelado''')
choice = int(input("digite sua escolha aqui: "))
if choice == 1 :
    off = (10/100) * price - price
    print('seu produto de {} por {} a vista'.format(price, off))
elif choice == 2:
    off = (0.5/100)* price - price
    print("seu produto no rotativo de {} fica por {}".format(price,off ))
elif choice == 3:
    off = (20 / 100 )* price + price
    print("seu produto parcelado de {} fica {} " . format(price, off))
