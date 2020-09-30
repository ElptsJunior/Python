print('\033[07m Create an program the get an value by user and show your multiplication table \033[m\n')
number = int(input('Little Locust , insert any number to start the multplication table:').title())
index = 1
while index < 11 :
    result = number*index
    print('\033[31m {}\033[m \033[35m x \033[m \033[32m {:2} \033[m = \033[4;34 m {}\033[m'.format(number, index, result))

    index = index + 1
