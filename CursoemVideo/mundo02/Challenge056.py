from datetime import date
older = 0
older_name = str
youngl = 0
year = date.today().year
for form in range(1, 5):
    print('\033[07m{}  Person   \033[m'.format(form))
    name = str(input("whats your name? "))
    gender = str(input("your gender [M / F ]:")).upper()
    born = int(input('when you born ?'))
    age = year - born
    age += 1
    if gender == 'M' and age > older :
        older = age
        older_name = name
    elif gender == 'F' and age < 20:
        youngl += 1

print(' the average of {} '.format(age/form))
print(' the name of older man was {} with {} years old '.format(older_name ,older))
print('How nany womens under twenty years old has on quiz ? total {}'.format(youngl))