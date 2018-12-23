def high_and_low(numbers):
    list1 = numbers.split()
    list2 = []
    for item in list1:
        x = int(item)
        list2.append(x)
    x = str(max(list2))
    y = str(min(list2))
    z = x + " " + y
    return z
