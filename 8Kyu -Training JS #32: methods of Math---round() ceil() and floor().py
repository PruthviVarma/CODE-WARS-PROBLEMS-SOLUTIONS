import math
def round_it(n):
    value = str(n)
    find_decimal_position = value.find('.')
    decimal_values = value[(find_decimal_position+1):]
    ###Ceil Function
    if(len(decimal_values)>len(value[0:find_decimal_position])):
        return math.ceil(n)
    ###Floor Function
    elif(len(decimal_values)<len(value[0:find_decimal_position])):
        return math.floor(n)
    ###Round Function
    elif(len(decimal_values)==len(value[0:find_decimal_position])):
        return round(n,0)
