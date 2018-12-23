def oddOrEven(arr):
    add = 0
    if(arr!=[0]):
        for num in arr:
            add = num + add
        if(add%2==0):
            return 'even'
        else:    
            return 'odd'
    else:    
        return arr
