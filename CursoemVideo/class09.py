array = '            My first range of strings               ' # if you wish create an empty list  insert variable[]
print(array)
print(array.__len__()) # this function show the lenght of the range
print('range'in array)# ask you is the condiction is True or False
print(array.find('first')) # find the string and show the string's position on range
print(array[9:14])
print(array.strip())# this function hide unecessary spaces, from the bouth sides
print(array.lstrip())# hide spaces from left side
print(array.rstrip())# hide spaces from right side
print(array.split()) #separe the word for block
print('*'.join(array)) # it's join the block word's spaces by inserted delimiter
print(array[9::25])
print(array[:25:2])# [begin:end:jump]
print(array.upper()) # change the strings to upper format
print(array.lower())# chage the strings to lower format
print(array.title())# Title format is when the firsr letter of block be in upper case
print(array.capitalize())# show's only de firt letter in upper case
print(array.count('f'))# count the total of result that search letther or word
print('............{}'.format(array))# replace the masc to object in array
print(array.find('androind'))# is an question if exist the string in arrey , if doont exist the result is iqual -1
print('android 'in array)# if the sentence it's rigth the result is True if in other hand False

