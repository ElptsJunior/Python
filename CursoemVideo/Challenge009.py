print('\033[07m Create an program the get an value by user and show your multiplication table \033[m\n')
number = int(input('Little Locust , insert any number to start the multplication table:').title())
index = 1
while index < 11 :
    result = number*index
    print('{} x {} = {}'.format(number, index, result))
    index = index + 1