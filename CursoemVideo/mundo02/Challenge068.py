from random import randint
wins = gamble = 0
while True:

    gamble = str(input('choose Pair or odd P/O  :')).split()[0].upper()
    if gamble != 'P' or 'O':
        while True:
            print('incorrect value, Please insert only P / O')
            gamble = str(input('choose Pair or odd P/0 :')).split()[0].upper()
            if gamble in 'P' or 'O':
                break
    choose = int(input(' insert an number'))
    cpu = randint(1, 100)
    if gamble in "P" and choose + cpu % 2 == 0 :
        print(f'You Won !you put{choose} and  cpu put {cpu} {sum(choose,cpu)} is Pair')
        wins += 1
    elif gamble in "O" and choose + cpu % 2 == 1:
        print(f'you won  you put {choose} and cpu put {cpu}{sum(choose, cpu)} is Odd')
        wins += 1
    else:
        print('You lose')
        break

print(f'''
end

Total of wins { wins }''')
