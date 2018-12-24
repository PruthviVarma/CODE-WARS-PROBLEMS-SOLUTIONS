def pillars(num_pill, dist, width):
    pass
    if(num_pill==1 or num_pill==0):
        return 0
    elif(num_pill==2):
        return dist*100
    elif(num_pill>=3):
        return (num_pill-1) * dist * 100 + (num_pill - 2) * width
        
