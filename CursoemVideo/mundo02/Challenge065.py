from time import sleep
numbers = int
maxi = 0
min = 999
index = 0
total = int
quiz = 'Y'
while index <= 6:
    numbers = int(input('type an number: '))
    if numbers > maxi:
        maxi = numbers
    elif numbers > -1:
        min = numbers
    total = numbers + numbers
    index += 1

print(' the average of numbers is {} '.format(total))
print(maxi, min)

