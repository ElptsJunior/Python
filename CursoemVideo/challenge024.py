print('='*200)
print("build an program that get an city name and answer if starts with 'santo' of not".title())
print('='*200)

city = str(input('Please insert an name of your city:').lower()).strip().split()

check = city[0] ==('santo')in city
print(check)