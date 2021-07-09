index = op = 0
while True:
    op = int(input('type the grade : '))
    if op <= -1 :
        break
    else:
         for index in range(1, 11):
             print(f'{op} x {index} = {op * index}')

print('end')