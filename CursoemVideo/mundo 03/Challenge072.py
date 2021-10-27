# Passo 1 : criar uma tupla totalmente preenchida de um a vinte por extenso.

extenso = ('zero','Um', 'Dois','Treis','Quatro','Cinco','Seis','Sete', ' Oito', 'Nove' ,'Dez', 'Onze', 'Doze','Treze'
              , 'quatorze',' Quinze', 'Dezesseis','Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# Passo 2: fazer o programa ler um numero pelo teclado ente 0 e 20

numero =int( input('digite um valor entre 0 e 20 :'))

# Passo 3 : validar se o numero digitado esta entre 0 e 20

while  numero < 0 or numero > 20:
    numero =int( input('numero errado, digite outro valor'))

# Passo 4: Mostrar o valor do numero digitado por extenso

print(extenso[numero])