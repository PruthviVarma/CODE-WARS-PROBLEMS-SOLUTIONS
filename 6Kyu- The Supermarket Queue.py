def queue_time(customers, n):
    # TODO
    #customers = [10,2,3,3],n=2
    #[10, 0]
    #[10, 2]
    #[10, 4]
    #[10, 7]
    #10
    
    #multiply the list with number of checkout tills
    l=[0]*n
    
    #for each customer
    for i in customers:
    
        l[l.index(min(l))] = l[l.index(min(l))] + i
    return max(l)
