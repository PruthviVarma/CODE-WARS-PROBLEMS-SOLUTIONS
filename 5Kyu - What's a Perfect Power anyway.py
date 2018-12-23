from math import log, sqrt
def isPP(n):
    if n==None: 
        return None
    square_root = round(sqrt(n),6)
    if square_root == round(square_root): 
        return [square_root, 2]
    for m in range(2,n):
        k = round(log(n, m),6)
        if k == round(k): 
            return [m, k]
  
 
