print(''' 
The same  professor of challenge 019 wants sort the him studantes of an presentation in class . buil an program 
that read four names and sort this names on screen .''')

from random import shuffle
index = 0 # for work's with whille loop
presentation_list =[]
speech = str

while index < 4:
    presentation_list.append(input(' Please insert your name '))
    print('Right')
    speech = presentation_list
    index = index + 1

print('This is the picked order of presentation is {}'.format(shuffle(speech)))