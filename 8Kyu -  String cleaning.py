def string_clean(s):
    """
    Function will return the cleaned string
    """
    # Your code here
    x = ''
    for i in s:
        if( i not in list(map(str,[0,1,2,3,4,5,6,7,8,9]))):
            x = x + i
    return x
