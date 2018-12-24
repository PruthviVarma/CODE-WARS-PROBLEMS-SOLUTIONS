import math
def century(year):
    # Finish this :)
    year = year/100;
    if(isinstance(year,(float))):
        return math.ceil(year)
    else:
        return year
