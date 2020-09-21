'''name = str(input('whats your name '))
if name == "Gustavo":
    print('Whats pretty name !')
else:
    print('your name is so ordinary!')
print('good morning, {}!'.format(name))# in python its mandatory let the last row empty
'''
print('='*130)
print("write an program that do your computer 'think' an integer number\n between zero and five and ask to user try to guess"
" whats the picked number:")
print('='* 130)
import random
sort = random.randint(0, 5)
guess = int(input('Hello little locust! pick an number between zero to five and try to guess the sorted number\n:'))
if guess == sort :
    print('Well done player ! the sorted {} number was the same as you choose{}'.format(sort,guess ))
else:
    print("Sorry player :( "
          ", The picked number {} don't match with the sorted by computer {} please try again ".format(guess,sort))
