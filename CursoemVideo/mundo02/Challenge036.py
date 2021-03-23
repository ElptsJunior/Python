# Declarando as variaveis
vcasa = float(input('Qual o valor que deseja financiar ? : '))
sal = float(input('Qual o valor do seu ultimo salário? :'))
anos = int(input('Pretende parcelar em quantos anos ?'))
prest = (vcasa) / (anos * 12 )
trinta = sal*0.30
#estutura aninhada

if prest == trinta:
    print('parabêns seu crédito foi aprovado ! ')
elif prest <= trinta:
    print(' seu crédito lhe permite financiar uma casa maior ')
else:
    print('que pena seu score está baixo tente uma casa mais barata ')
    #Mensagem que será exibida idependente da estrutura condicional aninhada
print(' Para Pagar uma casa no valor de {:.2f} em {} anos'.format(vcasa, anos))
print('a prestação será de {:.2f}'.format(prest))
