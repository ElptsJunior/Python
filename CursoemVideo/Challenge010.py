
print('\033[7m Build an program that ask how much reals do you have and convert to US$ \033[m \n')

real = float(input("what's Real's did you have in your wallet ?  : \n").title())
dollar = 5.25
cambio = real/dollar
print('\033[32m Sorry Little Locust did you have only {:2.3f} USR$ American dollar \033[m'.format(cambio))