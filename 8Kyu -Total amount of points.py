def points(games):
    total = 0
    for i in games:
        x,y = i.split(':')
        if(x>y):
            total = total + 3
        elif(x<y):
            total = total + 0
        elif(x==y):
            total = total + 1
    
    return total
