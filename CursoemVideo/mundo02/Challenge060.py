index = int(0)
arg = int(input('insert an number to find its factorial N!'))
index = arg
while index != 1:
    index -= 1
    fact = arg * index
    print('{}! = {} x {} = {}'.format(arg,arg,index,sum(fact)))