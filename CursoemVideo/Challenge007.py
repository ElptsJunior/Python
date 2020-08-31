"""
Build an program that read's two grades of an student,
and calculate and shows that average
"""
print('='*200)
av1 = (float(input('Welcome again, little Locust !,insert your Grade')))
av2 = (float(input('Please type the second Grade')))
avg = (av1 + av2)/2
print('The first Grade is {} and the second {}, you average is : {}'.format(av1, av2, avg))
print('='*200)
