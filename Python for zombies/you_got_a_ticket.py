car_speed =(int(input( ''' your car be in moviment... and you check your speed pannel,
what's your actual speed ?''')))

if car_speed > 110:
    print (' you got a ticket of the police officer!!')
    ticket_charge_value = 5*(car_speed - 110) 
    print (' congractulation your charger is ...',ticket_charge_value)
else:
    print( 'congractulation keep in speed limit! ')
