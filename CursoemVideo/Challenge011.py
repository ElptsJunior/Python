'''
Buil an program that calcules the height and width of the wall in meters,calculate its area and the quantitie
necessary of paint well khowing that one litre of ink colors 2 meters square  ( 2m²)
'''
height = float(input('Please insert the height  : '))
print('Ok, Height of {} meters '.format(height))
width = float(input('Now insert the width , please .. :'))
print('ok, width of {} meters '.format(width))
area = height*width
print(' your area is the {} meters powered of two'.format(area))
print('and the quantity litre necessary for collor all area is {}'.format(area/4))
