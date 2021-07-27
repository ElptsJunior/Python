total = 0
cashflow = int(input('how much to money to get?: '))

#while cashflow != 0:
if cashflow > 50 :
    rest = int( cashflow / 50)
    print(f'{rest} notes of 50 R$')
    total = cashflow - rest * 50
    print(total)
    if total > 20:
