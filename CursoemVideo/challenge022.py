print('''\n BULD AN PROGRAM, THAT GET THE FULL NAME OF USER, AND SHOW THIS TYPED NAME IN UPPER CASE, LOWER CASE,
TOTAL OF LETTER WITHOUT SPACES AND TOTAL OF LETTER OF FIRST NAME\n'''.title())

'''fullName = 'String Manipulator'
splited = fullName.split()




print( Your name in upper case: \n{0}\n
            Your name in lower case : \n{1}\n
            This is of total of letter without spaces \n {2} \n
            This is of total of letter of first name \n {3} \n 
      .format(fullName.upper(), fullName.lower(),splited.__len__(), splited[0].__len__()))

print(len(splited))
# pesquisar como somar os totais de letras em cada posisão do array splited com a função for somando cada range escaneado pelo len

'''
#answer key !
fullname = str(input('typing your name please:')).strip()
splited = fullname.split()
print('ok !')
print('work on it ....')
print('your name in upper case: {}'.format(fullname.upper()))
print('your name in lower case: {}'.format(fullname.lower()))
print('you name have {} letters'.format(len(fullname) - fullname.count(' ')))
print(' you name have {} letters:'.format(len(splited[0])))
#print('you name have {} letters:'.format(fullname.find(' ')
