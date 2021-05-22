'''sex = "null"
while sex != 'F':
    sex = str(input(' type your gender')).upper()
print('end program')'''

sex = str(input('type M/F : ')).upper().strip()[0]# This strip only get the first string inserted
while sex not in 'MF':
    print('incorrect value! Please try again')
    sex = str(input('type M/F :')).upper().strip()[0]
print(sex)