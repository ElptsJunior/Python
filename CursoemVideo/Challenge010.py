'''
Build an program that ask how much real's do you have and convert to US$
'''
real = float(input("what's Real's did you have in your wallet ?  :"))
dollar = 5.25
cambio = real/dollar
print('Sorry Little Locust did you have only {:2.3f} USR$ American dollar '.format(cambio))