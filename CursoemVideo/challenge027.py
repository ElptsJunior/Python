print('='* 130)
print('''BUILD A PROGRAM THAT READ THE KEYBOARD AND '''.title())
print('='* 130)
name = str(input('PLEASE LITTLE LOCUST, INSERT ANY WORD:\n'.capitalize())).strip().lower().split()
#lstname =.(name)
print('your first name is: {}'.format(name[0]))
print('your last name  is: {}'.format(name[len(name)-1]))# -1 BECAUSE WE DON'T WANTT COUNT THE POSITION ZERO
