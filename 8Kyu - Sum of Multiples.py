def sum_mul(n, m):
    if (n<=0 or m<=0):
        return 'INVALID'
    elif(n==m):
        return 0
    else:
        i = n
        sum = 0
        while i<m:
            sum = sum + i
            i = i + n
    return sum
            
