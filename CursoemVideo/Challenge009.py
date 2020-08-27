'''Create an program the get an value by user and show your multiplication table'''
number = int(input('Little Locust , insert any number to start the multilication table :  '))
index = 1
while index < 11 :
    result = number*index
    print('{} x {} = {}'.format(number, index, result))
    index = index + 1