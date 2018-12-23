def square_digits(num):
    x =  str(num)
    z = ""
    for item in x:
        y = int(item)**2
        z = z+str(y)
    return int(z)
