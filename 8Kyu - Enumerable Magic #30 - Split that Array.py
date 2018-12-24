def partition(list1, classifier_method):
    tup = ()
    list2 = []
    # Write your solution
    final_list1 = list(filter(classifier_method , list1)) 
    for i in list1:
            if(i not in final_list1):
                list2.append(i)
    tup = (final_list1,list2)
    return tup
