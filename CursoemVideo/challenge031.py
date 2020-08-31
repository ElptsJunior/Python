
distance = int(input('What your travel distance? :\n'))
price =int()
if distance <= 200 :
    price = 0.50
    print ('This price of travel is : \n your bill is : USD {} '.format(price * distance))
else:
    price = 0.45
    print('wow ! your travel deserved an discount \n your bill is : USD {}' .format( price *distance) )

