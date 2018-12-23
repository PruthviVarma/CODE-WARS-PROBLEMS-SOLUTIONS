def tickets(people):
    countof25 = 0
    countof50 = 0
    total = len(people)
    i = 0
    while(i<total):
        if(people[i]==25):
            countof25 = countof25 + 1
        elif(people[i]==50):
            countof50 = countof50 + 1
            countof25 = countof25 - 1
        else:
            if(countof50==0 and countof25>=3):
                countof25 = countof25 - 3
            else:
                countof50 = countof50-1
                countof25 = countof25-1
        i = i + 1
    
    if(countof50<0 or countof25<0):
        return "NO"
    else:
        return "YES"
        
