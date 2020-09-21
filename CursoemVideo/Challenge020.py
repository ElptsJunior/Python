print('''
Now the same professor of challenge 019.py  want's sort for an presentation of works ! build an program that read 4 
names and show in sorted order.  
''')
import random

index = 0
work_list = []

while index < 4:
   work_list.append(input(' Please little Locust a name : '))
   index = index + 1
print('Original list ', work_list)
random.shuffle(work_list)
print('List after first shuffle ', work_list)
random.shuffle(work_list)
print('List after Second Shuffle',work_list)

