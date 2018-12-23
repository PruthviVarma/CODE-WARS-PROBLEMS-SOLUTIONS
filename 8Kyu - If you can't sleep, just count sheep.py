def count_sheep(n):
    result = ""
    # your code
    if(n==1):
        result = "1 sheep..."
    else: 
        for i in range(1,n+1):
            result = result + str(i) + ' sheep...'
    
    return result
