minutes = int (input(' insert your call minutes'))
    if minutes <200:
    price = 0.20
    else:
    if minutes <= 400:
    price = 0.18
    if minutes >800:
    price = 0.08
    else:
    price =0.08
        
print("Phone bill: USD$ %6.2f" % (minutes * price))        





    
   
 
