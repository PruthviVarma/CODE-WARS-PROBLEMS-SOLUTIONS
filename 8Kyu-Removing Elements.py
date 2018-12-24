def remove_every_other(my_list):
    # Your code here!
    pass
    odd_list = [ x for x in range(len(my_list)) if x%2!=0]
    j = 0
    new_list = []
    for i in my_list:
        if j not in odd_list:
          new_list.append(i)
        j = j + 1
    return new_list
