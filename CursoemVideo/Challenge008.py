
print('\033[7m Build an program that can read in meters and convert in centimeters an milimeters\033[m')

meters = int(input('Welcome little Locust, insert the value to convert : '))
centimeters = meters*100
milimeter = meters*1000
print('The meters inserted was {} \n in centimeter is {} \n an milimeters {}'.format(meters, centimeters, milimeter))
