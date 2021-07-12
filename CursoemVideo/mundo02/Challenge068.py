from random import randint
wins = gamble = 0
while True:
    gamble = str(input('choose Pair or odd P/O')).split()[0].upper()
    cpu = randint(1, 100)
    if gamble in "P" and cpu % 2 == 0 :
        print(f'You Won ! {cpu} is Pair')
        wins += 1
    elif gamble in "O" and cpu % 2 == 1:
        print(f'you won {cpu} is Odd')
        wins += 1
    else:
        print('You loose')
        break

print(f'''
end

Total of wins { wins }''')
