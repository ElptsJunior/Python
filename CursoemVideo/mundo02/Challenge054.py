from datetime import date
maior = 0
menor = 0

update = date.today().year
for index in range(1,8):
    year = int(input("type {} your born age".format(index)))
    age = update - year
    if age >=  21:
        maior += 1


    else:
        menor += 1

print(' tivemos {} pessosas de maior idade'.format(maior))
print('tivemos {} pessoas menores de idade '.format(menor))