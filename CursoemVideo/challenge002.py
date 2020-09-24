print('\033[32m = \033[m'*27)
print(" BUILD AN PYTHON SCRIPT THAT READ'S DAY,MONTH AND YEAR AND RETURN  THE VALUES ".title())
print('\033[32m = \033[m'*27)

year = int(input('Please insert the year - yyyy :'))
month = int(input('Now insert the month - mm :'))
day = int(input('insert your day - dd : '))

print(' the date inserted  \033[7m{} / {} / {}\033[m isnt ? '.format(day, month, year))
