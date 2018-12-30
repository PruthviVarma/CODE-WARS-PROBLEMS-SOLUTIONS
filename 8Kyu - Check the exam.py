def check_exam(arr1,arr2):
    score = 0
    i = 0
    while(i<len(arr1)):
        if(arr2[i]!=""):
            if(arr1[i]==arr2[i]):
                score = score + 4
            else:
                score = score - 1
        i = i + 1
    if score>0:
        return score
    else:
        return 0
  
