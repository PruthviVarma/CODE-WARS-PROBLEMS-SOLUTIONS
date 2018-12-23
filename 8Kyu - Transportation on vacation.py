def rental_car_cost(d):
    # your code
    if(d==1 or d==2):
        return 40*d
    elif(d>=3 and d<7):
        return (40*d)-20
    elif(d>=7):
        return (40*d)-50
