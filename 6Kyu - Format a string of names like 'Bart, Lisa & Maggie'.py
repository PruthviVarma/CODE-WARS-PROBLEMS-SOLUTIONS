def namelist(names): 
    #assignments
    length_of_list = len(names)
    i = 0
    str1 = ""
    f = length_of_list - 1
    while i<length_of_list:
        m = names[i]
        k = m.popitem()
        n = k[1]
        if i ==0:
            str1 = n
        elif f==i:
            str1 = str1 + " & " + n
        else:
            str1 = str1 + ", "+n
        i = i + 1
        
    return str1
