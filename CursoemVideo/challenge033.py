first = int(input(' Please little Locust, insert the first number:'))
second = int(input('Now, typing the second number: '))
third = int(input('right! now insert the last one Please'))
bigger = int()
lower = int()
if first > second and third :
    bigger = first
else:
    first < second and third
    lower = first
    if first == second == third:
        print("it's not fare ! iqual number's ")
if second > first and third:
    bigger = second
else:
    second < first and third
    lower = second
if third > second and first:
    bigger = third
else:
    third < second and first
    lower = third

print('.')
print('..')
print('...')
print('.... ok ! the number {} was the bigger value insert and the {} was the lower value insert  '.format(bigger,lower))