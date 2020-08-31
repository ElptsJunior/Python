salary = int(input("What's your salary : \n"))
if salary > 1250:
    salary = salary + salary * 0.10
    print('your raise was 10% total {}'.format(salary))
else:
    salary = salary + salary * 0.15
    print('your raise was 15% total {}'.format(salary))