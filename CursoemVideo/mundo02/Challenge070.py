name = namef = product = total = little = overhundred = 0
while True:
    name = str (input('name of product? :'))
    product = float(input('price R$: '))
    total += product
    keep = str( input('did you what to continue [y / N]')).split()[0].upper()
    little = p
    #while keep != 'Y' or 'N':
     #   keep = str(input('did you what to continue??')).split()[0].upper()
    if keep == "N":
        break
    else:
        if product > 1:
            little = product
        if little > product:
            little = product
            namef = name
        if product > 1000:
            overhundred += 1


print(f'tota of product was { total}')
print(f' was { overhundred }')
print(namef)
