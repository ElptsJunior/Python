print('='*130)
print('build an script that read an number an show your previous and next number:'.title())
print('='*130)

number = int(input('Insert any number: \n'))
print(' The inserted number was {} and you previus is : {} and the next valuer is :{}'.format(number, number-1, number+1).capitalize())