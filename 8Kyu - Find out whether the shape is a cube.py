def cube_checker(volume, side):
    if(volume<=0):
        return False
    elif(volume == pow(side,3)):
        return True
    else:
        return False
