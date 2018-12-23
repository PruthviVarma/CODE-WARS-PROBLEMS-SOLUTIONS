def isValidWalk(walk):
    north = 0
    south = 0
    east = 0
    west = 0
    if(len(walk)==10):
        for i in range(0,len(walk)):
            if(walk[i]=='n'):
                north = north + 1
            elif(walk[i]=='s'):
                south = south + 1
            elif(walk[i]=='e'):
                east = east + 1
            else:
                west = west + 1
                
        if(north == south and east == west):
            return True
        else:
            return False
                
    else:
        return False
