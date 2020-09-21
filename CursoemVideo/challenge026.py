print('='* 200)
print('''Build a program that read an frase by keyboard and show how many times the letter "A", \n
      'appears and what your position it's first time and last time it's appears .'''.capitalize())
print('='*200)
a = str(input('Please little locust! insert any commented as you wish, come on ! feel comfortable:\n ')).strip().lower()
task = a.count('a')
print('''The letter "A" apper in frase : {} times
The first time the letter "A" appears was{} :position.
The last time was founded in  position of {} string'''.format(a.count('a'), a.find('a')+1, a.rfind('a')+1))