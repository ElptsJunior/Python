print("""
The Professor want's to sort one of four student  to cleaning the blackboard ,build an program that help's him reading the
name of student and show the picked name .
""")
import random
index = 0
list = []

while index < 4 :   # looping of four input's and saving in an array by append
   list.append(input('insert your name : '))
   index += 1
picked = random.choice(list) # indented out of while range
print('The Studend chosen was : {} '.format(picked))