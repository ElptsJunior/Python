
add = 0
index = 1
while True: # fist the program need check is condicion is true#
    insert = int(input(" calc the average that Number's %d  press 0 for exit ."%index))
    if  insert == 0:    
        break
    add = add + insert
    index = index + 1
print (" Average (%d)" % (add/index))

''' this joker %d
show's the variable inserted on same lime mirror by % this help's for dont create
an variable avg = add/index used in java for example .'''
