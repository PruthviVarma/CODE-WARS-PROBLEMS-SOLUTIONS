def multi_table(number):
    x = ""
    for i in range(1,11):
        x = x + str(i) + " * " + str(number) + " = " + str(number*i) + "\n"
    return x.rstrip('\n')
