from time import sleep
numbers = 0
index = 0
total = 0
quiz = ''
while quiz != 'N':
    numbers = int(input('type an number: '))
    total = numbers + numbers
    index += 1
    quiz = input('Did you want to continue insert news numbers? Y/N :').upper()[0].split()
quiz = quiz
print('end')
print('the average of number is {}'.format(index / total))
sleep(3)
print(' the max value is {}'.format(max(numbers)))
sleep(2)
print(' the min is {} '.format(min(numbers)))