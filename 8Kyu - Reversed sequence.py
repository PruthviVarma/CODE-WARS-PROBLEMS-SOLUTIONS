def reverse_seq(n):
    if(n>0 and n==1):
        return [1]
    elif(n<=0):
        return []
    else:
        return [x for x in reversed(range(1,n+1))]
