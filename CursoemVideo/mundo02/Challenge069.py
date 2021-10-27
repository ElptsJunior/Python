gender = yearold = keep = under20 = over18 = male =  0
while True:
    yearold = int(input('How old are you ? '))
    gender = "  "
    while gender not in 'MF': #forcar a validacao de m ou f
        gender = str(input('Male or female ? M / F')).split()[0].upper()
    keep = str(input(' did you whant to continue ? Y / N')).split()[0].upper()
    if keep in 'N':
        break
    else:
        if yearold > 18 :
            over18 += 1
            if gender == 'M':
                male += 1

            elif gender == 'F' and yearold < 20:
                under20 += 1

print( f'A) Total of people over 18 years old was { over18 }')
print(f' B) How manny Men was cadastred ? { male }')
print(f' c) How manny womens under 20 years old ? {under20} ')
