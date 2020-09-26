print('\033[32m = \033[m'* 25)
print('build an script that read an number an show your previous and next number:'.title())
print('\033[32m = \033[m'*25)

number = int(input('Insert any number: \n'))
print(' The inserted number was {} and you previus is : \033[4;{} and the next valuer is :{}'.format(number, number-1, number+1).capitalize())