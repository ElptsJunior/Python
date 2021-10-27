# Podemos iniciar uma variavel composta de tres maneiras
# com  parenteses  ()
# com colchetes []
# ou com chaves {}  lembrando que parenteses sao para tuplas , colchetes sao para listas e chaves para dicionarios em python

lanche = ('hamburguer' , 'suco','pizza','pudim')
#Tuplas sao imutaveis enquanto se esta em execucao
print(lanche )

# referenciando uma variavel em especifico , mesmo sendo uma tupla com parenteses o fateamento sempre sera com colchetes mais a posisao do indice

#print (lanche[1]) = 'refrigerante'

for index in range(0, len(lanche)):
    print(lanche[index])

