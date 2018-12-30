def multiple_of_index(arr):
    new_list = []
    for i,a in enumerate(range(len(arr))):
        if(i!=0):
           if(arr[i]%i == 0 and i>0):
                new_list.append(arr[i])
    return new_list
