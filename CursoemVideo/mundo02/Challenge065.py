
avg = total = capther = bigger = smaller = 0
keep = 'Yy'
while keep in 'Yy':
    numbers = (int(input('type an number: ')))
    capther += 1
    total += numbers
    if capther == 1:
        bigger = smaller = numbers # when one number is inserted this is the smaller and bigger

    else:
         if numbers > bigger:
            bigger = numbers
         elif numbers < smaller:
             smaller = numbers

    keep=input("you whant to continue? Y/ N").split()[0]
print('you typed {} numbers'.format(capther))
print(' the average between is {}'.format(total/capther))
print(' the bigger number is {} and the little is {}'.format(max(smaller, bigger), min(smaller, bigger)))

print('end')


