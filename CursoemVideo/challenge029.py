print('')
print('')
print('')
ticket = 7
speedlimit = 80
speed = int(input("What's your car speed? "))
if speed > speedlimit:
    print('you got a ticket to ride ! the value of ticket was {} Dollars '.format((speed - speedlimit)* ticket))
