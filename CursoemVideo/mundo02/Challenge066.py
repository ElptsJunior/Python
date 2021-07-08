from time import sleep
index = num = summ = 0
while True: # aqui eu deixo o loop infinito
   num = int(input('insert an number , if you whant to exit type 999:  '))
   if num == 999: # nessa condicao sera feita primeira a verificacao sem que o flag entre na soma
       print('Flag activaded !')
       break
   else:
       summ += num
       index += 1
print('end program')
sleep(3)
print(f'the total of numbers inserted was {index} and the summation was {summ}')