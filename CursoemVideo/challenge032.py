
from datetime import date
leapyear = int(input("what year do you want to analise? if the current year just press '0' \n"))
if leapyear == 0:
    leapyear = date.today().year
if leapyear % 400 == 0  or leapyear % 4 == 0 and leapyear %100!= 0 :
    print('This year is an leapyear ! ')
else:
    print(" This year dont is an leapyear")