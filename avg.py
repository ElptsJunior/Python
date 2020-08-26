counter = 1
acumulater = 0

# the diferencer between an counter and acumulater is the counter get constant#
# and sequecial datas than acumalater that reciave variables#

while counter <= 10 :
    var = int ( input("insert the %d number: " %counter))
    acumulater = acumulater+ var
    counter = counter+1
print ( " average: %5.2f" %(acumulater/10))    
    
