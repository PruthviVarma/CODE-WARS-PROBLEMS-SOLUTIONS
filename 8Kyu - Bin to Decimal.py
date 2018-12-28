def bin_to_decimal(inp):
    inp = int(inp)
    decimal, i, n = 0, 0, 0
    while(inp != 0): 
        dec = inp % 10
        decimal = decimal + dec * pow(2, i) 
        inp = inp//10
        i += 1
    return decimal
