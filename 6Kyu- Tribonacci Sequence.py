def tribonacci(signature, n):
    #your code here
    a = 0
    b = 0
    c = 0
    d = 0
    i = 0
    list1 = []
    if(n==0):
    #return empty list
        return []
    elif(n==1):
    #return only first element
        list1.append(signature[0])
        return list1
    elif(n==2):
    #return only 2 elements
        list1.append(signature[0])
        list1.append(signature[1])
        return list1
    else:
    #return all the elements
        for i in range(0,len(signature)):
            if(i == 0):
                a = signature[i]
                list1.append(a)
            elif(i == 1):
                b = signature[i]
                list1.append(b)
            else:
                c = signature[i]
                list1.append(c)
            
        while i < n-1:
            d = a + b + c
            list1.append(d)
            a = b
            b = c
            c = d
            i = i + 1
            
        return list1
