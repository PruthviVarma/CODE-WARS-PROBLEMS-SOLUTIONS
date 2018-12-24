def nearest_sq(n):
    # pass
    if(n == 1 or n == 2):
        return 1
    else:
        for i in range(3,n+1):
            if(i**2>=n):
                x = i**2 - n
                y = n -(i-1)**2
                if(y<x):
                    return (i-1)**2
                else:
                    return i**2
