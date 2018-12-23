def iq_test(numbers):
    #your code here
    count_even = 0
    count_odd = 0
    a = 0
    b = 0
    list1=[]
    position = 0
    for i in numbers.split():
        if(int(i)%2==0):
            count_even = count_even + 1
            a = i
        else:
            count_odd = count_odd + 1
            b = i
    
    if(count_odd == 1):
        list1 = list(numbers.split())
        position = list1.index(b)
        position = position + 1
        return position
    elif(count_even == 1):
        list1 = list(numbers.split())
        position = list1.index(a)
        position = position + 1
        return position
    else:
        return 0
