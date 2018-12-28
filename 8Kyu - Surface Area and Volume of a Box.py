def get_size(w,h,d):
    #your code here
    #volume of box
    v = w*h*d
    s = 2*w*h + 2*h*d + 2*d*w
    
    return [s,v]
